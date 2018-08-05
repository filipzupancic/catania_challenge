import helper

BOT_WORD = '/marvin'
PROJECT_PK_WORD = 'projectPK'
MARVEL_TOKEN_WORD = 'marvelToken'

# file contains messages that are sent when new event occurs in application
# and we want to notify a user

# sends a notification about edit on project
def edit_message(screen_name, project_link, card_id, user_id):
    if project_link is not None:
        link = "Go to project: " + project_link
    else:
        link = ""
    message = "Changes made on screen #" + screen_name + "#.\n\n" + link
    helper.post(message, card_id, None, user_id)


# sends a notification about new comment on project
def comment_message(user_name, screen_name, project_link, comment, card_id, user_id):
    if project_link is not None:
        link = "Go to project: " + project_link
    else:
        link = ""
    message = user_name + " added new comment on screen #" + screen_name + "#. " + "\n\n@ " + comment + " @\n\n" + link
    helper.post(message, card_id, None, user_id)


# sends a notification that new screen was created inside the project
def create_message(screen_name, project_link, card_id, user_id):
    if project_link is not None:
        link = "Go to project:\n" + project_link
    else:
        link = ""
    message = "New screen #" + screen_name + "# was created.\n\n" + link
    helper.post(message, card_id, None, user_id)


# sends list of bor actions
def bot_initial_message(card_id, user_id):
    upload_file_response = helper.upload_file("img/marvin.png", helper.BOT_ID)
    helper.post("", card_id, upload_file_response.id, user_id)
    message = "I accept messages that start with /marvin.\n" \
              "For project number type" + PROJECT_PK_WORD + " [project number] and for marvel token type" + \
              MARVEL_TOKEN_WORD + " [marvel token]."
    helper.post(message, card_id, None, user_id)
