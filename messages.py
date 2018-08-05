import helper

BOT_WORD = '/marvin'
PROJECT_PK_WORD = 'projectPK'
MARVEL_TOKEN_WORD = 'marvelToken'
MAIL_UPDATE_WORD = ' hitMe'
MARVIN_PIC_ID = 'TF_eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiNTQzIiwiZmlsZV9kYXRhX2luZm8iOiJHRE56QjhiZTllOTJyLVNDUVUtNkFmbUktaVlmdnF1V0k0SkUyYktIY0pZLjE4Y0Y7bWFydmluLnBuZzsxODsxODhlOzFkNDJjYTY1NGYyYjkwMjt2IiwibmJmIjoxNTMzNDY0NjAwLCJleHAiOjE1MzM0NjgyMDAsImlhdCI6MTUzMzQ2NDYwMH0.ZPhvYkhH-yhbLoftRpPA1Nb829LoyLLroUxS0RFpCUY'

EMOTICON_ROBOT = "\uD83E\uDD16"
EMOTICON_COMMENT = "\uD83D\uDCAC"
EMOTICON_EDIT = "\u270F\uFE0F"
EMOTICON_NEW = "\uD83D\uDCCC"
EMOTICON_OK = "\uD83C\uDD97"


# file contains messages that are sent when new event occurs in application
# and we want to notify a user

# sends a notification about edit on project
def edit_message(screen_name, screen_link, card_id, user_id):
    if screen_link is not None:
        link = "Go to screen: " + screen_link
    else:
        link = ""
    message = EMOTICON_EDIT + "  Changes made on screen #" + screen_name + "#.\n" + link
    helper.post(message, card_id, None, user_id)


# sends a notification about new comment on project
def comment_message(user_name, screen_name, screen_link, comment, card_id, user_id):
    if screen_link is not None:
        link = "Go to screen: " + screen_link
    else:
        link = ""
    message = EMOTICON_COMMENT + "  " + user_name + " commented '" + comment + "' on screen #" + screen_name + "#\n"+ link
    helper.post(message, card_id, None, user_id)


# sends a notification that new screen was created inside the project
def create_message(screen_name, screen_link, card_id, user_id):
    if screen_link is not None:
        link = "Go to screen:" + screen_link
    else:
        link = ""
    message = EMOTICON_NEW + "  " + "New screen #" + screen_name + "# was created.\n" + link
    helper.post(message, card_id, None, user_id)


# sends list of bot actions
def bot_initial_message(card_id, user_id):
    #upload_file_response = helper.upload_file("img/marvin.png", helper.BOT_ID)
    #uMARVIN_PIC_ID = pload_file_response.id
    #helper.post("", card_id, MARVIN_PIC_ID, user_id)
    helper.post("\uD83E\uDD16", card_id, None, user_id)
    message = "I accept messages that start with /marvin.\n" \
              "To send you updates I need project number and Marvel token.\n" \
              "For project number type " + PROJECT_PK_WORD + " [project number]\nand for Marvel token type " + \
              MARVEL_TOKEN_WORD + " [marvel token]."
    helper.post(message, card_id, None, user_id)

# sends user data valid message
def user_data_valid_message(card_id, user_id):
    message = EMOTICON_OK + "Now I have the project number and the Marvel token,\n" \
              "I will keep you updated for this project"
    helper.post(message, card_id, None, user_id)
    return

# sends wrong Marvel token message
def wrong_marvel_token_message(card_id, user_id):
    message = "I am having troubles getting data from Marvel.\n" \
              "Is the Marvel token correct?" \
              "Type " + MARVEL_TOKEN_WORD + " [marvel token] to update the token."
    helper.post(message, card_id, None, user_id)
    return

# sends wrong project number message
def wrong_project_number_message(card_id, user_id):
    message = "I cannot find the project.\n" \
              "Please update the project number by " + PROJECT_PK_WORD + " [project number]."
    helper.post(message, card_id, None, user_id)
    return

def wrong_data_message(card_id, user_id):
    message = "I do not have all data required to process this operation.\n " \
              "Please tell me project number and marvel token."
    helper.post(message, card_id, None, user_id)
    return
