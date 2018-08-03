def get_comments(pk):
    query_string = """
    { "query" : "
        fragment commentInfo on CommentNode {
          pk
          createdAt
          message
          author {
            username
          }
          annotation {
            posX
            posY
            label
          }
          status {
            markedAt
            markedBy {
              username
            }
            resolved
          }
        }

        query getComments($projectPk: Int!) {
          project(pk: $projectPk) {
            pk
            name
            screens(first: 1) {
              edges {
                node {
                  displayName
                  comments(first: 2) {
                    edges {
                      node {
                        ...commentInfo
                        children(first: 3) {
                          edges {
                            node {
                              ...commentInfo
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
    ",
    "variables" : 
        {"projectPk" : """ + pk + """}
    }
    """
    return query_string.replace('\n', '')

def project_last_modified(pk):
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

def screens_last_modified(pk):
    query_string = """
            { "query" : "
                query {
                  project(pk: """ + pk + """) {
                    screens {
                      edges {
                        node {
                          displayName
                          modifiedAt
                          uuid
                          uploadUrl
                        }
                      }
                    }
                  }
                }
            "}
            """
    return query_string.replace('\n', '')

def get_comments_after(pk, cursor):
    query_string = """
                { "query" : "
                    query {
                      project(pk: """ + pk + """) {
                        screens {
                          edges {
                            node {
                              displayName
                              comments(after: \"""" + cursor + """\" last:10) {
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




def chandler_ping():
    resp = requests.post(MARVEL_API_URL, data=screens_last_modified(project_id),
                         headers={"Authorization": "Bearer " + MARVEL_TOKEN})
    screens = resp.json()['data']['project']['screens']['edges']
    new_modifiedAt = 0
    for i in screens:
        screen_modified_time = time.mktime(time.strptime(i['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))
        if screen_modified_time > new_modifiedAt:
            new_modifiedAt = screen_modified_time
            last_modified_screen = i

    return last_modified_screen



last_modified_screen = chandler_ping()
old_modifiedAt = time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))

while True:
    last_modified_screen = chandler_ping()
    new_modifiedAt = time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))

    if new_modifiedAt != old_modifiedAt:
        screen_id = re.findall(r"\d+", last_modified_screen['node']['uploadUrl'])[0]
        screen_url = "https://marvelapp.com/project/"+project_id+"/screen/"+screen_id+"/"
        print(last_modified_screen['node']['displayName'] + " was modified - time:" + last_modified_screen['node']['modifiedAt'])

        messages.edit_message("Somebody", last_modified_screen['node']['displayName'], screen_url, chat.id, user_id)
        old_modifiedAt = new_modifiedAt
    else:
        time.sleep(1)