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

def query_string__get_comments_after_cursor(project_id, comment_cursor):
    query_string = """
                { "query" : "
                    query {
                      project(pk: """ + project_id + """) {
                        screens {
                          edges {
                            node {
                              displayName
                              comments(after: \"""" + comment_cursor + """\" last:10) {
                                edges {
                                  cursor
                                  node {
                                    createdAt
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
# QUERY STRINGS end


# CLASSES start
class Screen:
  def __init__(self, screen_marvel_object, project_id):
    self.pk = screen_marvel_object['node']['pk']
    self.modifiedAt_time  = time.mktime(time.strptime(screen_marvel_object['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))
    self.modifiedAt  = screen_marvel_object['node']['modifiedAt']
    self.screen_id = re.findall(r"\d+", screen_marvel_object['node']['uploadUrl'])[0]
    self.screen_url = "https://marvelapp.com/project/" + project_id + "/screen/" + self.screen_id + "/"
    self.displayName = screen_marvel_object['node']['displayName']
# CLASSES end


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

def check_if_new_comments(marvel_api_url, marvel_token, project_id, screen_pk, comment_cursor):
    resp = requests.post(marvel_api_url, data=query_string__get_comments_after_cursor(project_id, comment_cursor),
                         headers={"Authorization": "Bearer " + marvel_token})
    #TODO