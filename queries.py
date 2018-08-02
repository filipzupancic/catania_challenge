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