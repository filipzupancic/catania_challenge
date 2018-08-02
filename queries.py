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