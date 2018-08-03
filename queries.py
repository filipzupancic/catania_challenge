import requests
import time
import re

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
def check_if_screen_modified(marvel_api_url, marvel_token, project_id, old_modifiedAt):
    last_modified_screen = get_last_modified_screen(marvel_api_url, marvel_token, project_id)
    new_modifiedAt = time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))
    modified_screen = None

    if new_modifiedAt != old_modifiedAt:
        modified_screen = Screen(last_modified_screen, project_id)

    return modified_screen
# DEMO CODE
'''
import queries
import time
import messages
import helper

MARVEL_TOKEN = "bUfITrzmkkWMiCSgKy0NWMsu9E0imV"
MARVEL_API_URL = "https://api.marvelapp.com/graphql/"
project_id = "3246216"

user_id = helper.get_user_id_by_email(helper.USER1_MAIL)
chat = helper.get_chat(helper.USER1_MAIL, user_id)

last_modified_screen = queries.get_last_modified_screen(MARVEL_API_URL, MARVEL_TOKEN, project_id)
old_modifiedAt = time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))

while True:
    modified_screen = queries.check_if_screen_modified(MARVEL_API_URL, MARVEL_TOKEN, project_id, old_modifiedAt)

    if modified_screen is not None:

        print(modified_screen.displayName + " was modified - time:" + modified_screen.modifiedAt)
        messages.edit_message("Somebody", modified_screen.displayName, modified_screen.screen_url, chat.id, user_id)

        old_modifiedAt = modified_screen.modifiedAt_time

    time.sleep(1)
'''

comment_cursors = {}
def check_for_new_comments(marvel_api_url, marvel_token, project_id):
    new_comments = None
    screen_name = None
    screen_url = None

    resp0 = requests.post(marvel_api_url, data=query_string__get_screens(project_id),
                          headers={"Authorization": "Bearer " + marvel_token})

    screen_edges = resp0.json()['data']['project']['screens']['edges']
    for screen_edge in screen_edges:
        screen_pk = str(screen_edge['node']['pk'])

        if screen_pk in comment_cursors.keys():
            # get comments after cursor
            resp = requests.post(marvel_api_url,
                                  data=query_string__get_comments_after_cursor(project_id, comment_cursors[screen_pk], 50),
                                  headers={"Authorization": "Bearer " + marvel_token})
        else:
            # set comment_cursors[screen_pk] to the last cursor (initialize cursor for this screen)
            resp = requests.post(marvel_api_url, data=query_string__get_comments_after_cursor(project_id, "", 1),
                                 headers={"Authorization": "Bearer " + marvel_token})

        for screen_edge in resp.json()['data']['project']['screens']['edges']:
            screen = screen_edge['node']
            if str(screen['pk']) == screen_pk:
                if len(screen['comments']['edges']) > 0:
                    if screen_pk in comment_cursors.keys():
                        # if comment_cursors for this screen already exists, then we have new comments
                        # do sth with the new comments:
                        new_comments = screen['comments']['edges']
                        screen_name = screen['displayName']
                        screen_url = get_screen_url(project_id, screen['uploadUrl'])+"comments/"
                    comment_cursors[screen_pk] = screen['comments']['edges'][0]['cursor']
                break

    return (new_comments, screen_name, screen_url)
# DEMO CODE
'''
import queries
import time
import messages
import helper

MARVEL_TOKEN = "bUfITrzmkkWMiCSgKy0NWMsu9E0imV"
MARVEL_API_URL = "https://api.marvelapp.com/graphql/"
project_id = "3246216"

user_id = helper.get_user_id_by_email(helper.USER1_MAIL)
chat = helper.get_chat(helper.USER1_MAIL, user_id)

last_modified_screen = queries.get_last_modified_screen(MARVEL_API_URL, MARVEL_TOKEN, project_id)
old_modifiedAt = time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))

while True:
    new_comments, screen_name, screen_url = queries.check_for_new_comments(MARVEL_API_URL, MARVEL_TOKEN, project_id)

    if new_comments is not None:
        for i in new_comments:
            new_comment = i['node']
            print(new_comment['author']['username'] + "  commented :" + new_comment['message'])
            messages.comment_message(new_comment['author']['username'], screen_name,
                                     screen_url, new_comment['message'], chat.id, user_id)

    time.sleep(1)
'''