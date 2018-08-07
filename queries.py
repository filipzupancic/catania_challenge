import requests
import time
import re
from copy import deepcopy

# QUERY STRINGS start
def query_string__project_last_modified(pk):
    query_string = """
        { "query" : "
            query {
              project(pk: """ + pk + """) {
                modifiedAt
              }
            }
        "}
        """
    return query_string.replace('\n', '')

def query_string__screens_last_modified(pk):
    query_string = """
            { "query" : "
                query {
                  project(pk: """ + pk + """) {
                    screens {
                      edges {
                        node {
                          pk
                          displayName
                          modifiedAt
                          uploadUrl
                        }
                      }
                    }
                  }
                }
            "}
            """
    return query_string.replace('\n', '')

def query_string__get_comments_after_cursor(project_id, comment_cursor, last):
    query_string = """
                { "query" : "
                    query {
                      project(pk: """ + project_id + """) {
                        screens {
                          edges {
                            node {
                              pk
                              displayName
                              uploadUrl
                              comments(after: \\\"""" + comment_cursor + """\\\" last:""" +str(last)+ """) {
                                edges {
                                  cursor
                                  node {
                                    message
                                    author {
                                      username
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                "}
                """
    return query_string.replace('\n', '')

def query_string__get_screens(pk):
    query_string = """
        { "query" : "
            query {
              project(pk: """ + pk + """) {
                screens {
                  edges {
                    node {
                      pk
                      displayName
                      uploadUrl
                    }
                  }
                }
              }
            }
        "}
        """
    return query_string.replace('\n', '')
# QUERY STRINGS end


# CLASSES start
class Screen:
  def __init__(self, screen_marvel_object, project_id):
    self.pk = screen_marvel_object['node']['pk']
    self.modifiedAt_time  = time.mktime(time.strptime(screen_marvel_object['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))
    self.modifiedAt  = screen_marvel_object['node']['modifiedAt']
    self.screen_url = get_screen_url(project_id, screen_marvel_object['node']['uploadUrl'])
    self.displayName = screen_marvel_object['node']['displayName']
# CLASSES end

# VALIDATING USER DATA
# returns {int}:
#    0 - data valid
#    1 - request failed (probably wrong marvel token)
#    2 - no project found (wrong project pk)
def check_user_data(marvel_api_url, card):
    resp = requests.post(marvel_api_url, data=query_string__project_last_modified(card.project_pk),
                         headers={"Authorization": "Bearer " + card.marvel_token})
    if (resp.status_code != 200):
        return 1
    if (resp.json()['data']['project'] == None):
        return 2
    return 0


def get_screen_url(project_id, screen_upload_url):
    return "https://marvelapp.com/project/" + project_id + "/screen/" + re.findall(r"\d+", screen_upload_url)[0] + "/"

def get_last_modified_screen(marvel_api_url, marvel_token, project_id):
    resp = requests.post(marvel_api_url, data=query_string__screens_last_modified(project_id),
                         headers={"Authorization": "Bearer " + marvel_token})
    screens = resp.json()['data']['project']['screens']['edges']
    new_modifiedAt = 0
    last_modified_screen = None

    for i in screens:
        screen_modified_time = time.mktime(time.strptime(i['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))
        if screen_modified_time > new_modifiedAt:
            new_modifiedAt = screen_modified_time
            last_modified_screen = i

    return last_modified_screen

# this function returns
#  - None if no screen is changed, or
#  - last modified screen as 'Screen' object if a screen was modified after the 'old_modifiedAt'
def check_if_screen_modified(marvel_api_url, card):
    last_modified_screen = get_last_modified_screen(marvel_api_url, card.marvel_token, card.project_pk)
    if last_modified_screen is None:
        return None

    if card.old_modifiedAt_screen is None:
        # initialize old_modifiedAt
        card.change_old_modifiedAt_screen(time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00")))
        return None

    new_modifiedAt = time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))
    modified_screen = None

    if new_modifiedAt != card.old_modifiedAt_screen:
        modified_screen = Screen(last_modified_screen, card.project_pk)
        card.change_old_modifiedAt_screen(modified_screen.modifiedAt_time)

    return modified_screen

# this function returns
#  - None if there is no new comments, or
#  - a tuple of (new_comments, screen_name, screen_url)
#       new_comments = array of 'CommentEdge'
#       screen_name = string - display name of the screen
#       screen_url = string - url to comment section of the screen
def check_for_new_comments(marvel_api_url, card):
    new_comments = None
    screen_name = None
    screen_url = None

    resp0 = requests.post(marvel_api_url, data=query_string__project_last_modified(card.project_pk),
                          headers={"Authorization": "Bearer " + card.marvel_token})
    new_modifiedAt = time.mktime(time.strptime(resp0.json()['data']['project']['modifiedAt'][0:19], "%Y-%m-%dT%H:%M:%S"))

    if (card.old_modifiedAt_project == new_modifiedAt):
        return (new_comments, screen_name, screen_url)

    card.old_modifiedAt_project = new_modifiedAt

    resp1 = requests.post(marvel_api_url, data=query_string__get_screens(card.project_pk),
                          headers={"Authorization": "Bearer " + card.marvel_token})
    screen_edges = resp1.json()['data']['project']['screens']['edges']

    for screen_edge in screen_edges:
        screen_pk = str(screen_edge['node']['pk'])

        if screen_pk in card.comment_cursors.keys():
            # get comments after cursor
            resp = requests.post(marvel_api_url,
                                  data=query_string__get_comments_after_cursor(card.project_pk, card.comment_cursors[screen_pk], 50),
                                  headers={"Authorization": "Bearer " + card.marvel_token})

            for screen_edge2 in resp.json()['data']['project']['screens']['edges']:
                screen = screen_edge2['node']
                if str(screen['pk']) == screen_pk:
                    if len(screen['comments']['edges']) > 0:
                        if screen_pk in card.comment_cursors.keys():
                            # if comment_cursors for this screen already exists, then we have new comments
                            # do sth with the new comments:
                            new_comments = screen['comments']['edges']
                            screen_name = screen['displayName']
                            screen_url = get_screen_url(card.project_pk, screen['uploadUrl'])+"comments/"
                    break

    # get last cursors
    resp2 = requests.post(marvel_api_url, data=query_string__get_comments_after_cursor(card.project_pk, "", 1),
                          headers={"Authorization": "Bearer " + card.marvel_token})
    screen_edges = resp2.json()['data']['project']['screens']['edges']
    
    for screen_edge in screen_edges:
        screen_pk = str(screen_edge['node']['pk'])
        screen = screen_edge['node']
        if len(screen['comments']['edges']) > 0:
            card.comment_cursors[screen_pk] = screen['comments']['edges'][0]['cursor']
        else:
            card.comment_cursors[screen_pk] = ""

    return (new_comments, screen_name, screen_url)


def check_for_new_screens(marvel_api_url, card):
    new_screens = None

    resp1 = requests.post(marvel_api_url, data=query_string__get_screens(card.project_pk),
                          headers={"Authorization": "Bearer " + card.marvel_token})
    screen_edges = resp1.json()['data']['project']['screens']['edges']

    if card.screen_list is None:
        card.screen_list = screen_edges
        return None

    if len(card.screen_list) < len(screen_edges) and card.screen_list != screen_edges:
        new_screens = deepcopy([d for d in screen_edges if d not in card.screen_list])
        for new_screen in new_screens:
            new_screen['node']['uploadUrl'] = get_screen_url(card.project_pk, new_screen['node']['uploadUrl'])

        last_modified_screen = get_last_modified_screen(marvel_api_url, card.marvel_token, card.project_pk)
        new_modifiedAt = time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))
        card.change_old_modifiedAt_screen(new_modifiedAt)

        card.screen_list = screen_edges

    return new_screens