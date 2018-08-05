#import loop_sdk_client as loop_api
#from loop_sdk_client import api_client
#from loop_sdk_client import configuration as config
import requests
import json

import loop_sdk_client as loop_api
# from loop_sdk_client.rest import ApiException

loop_api_host = "https://clean-sprint-app.intheloop.io"

loop_api.Configuration().host = loop_api_host
BOT_MAIL = "cataniabot@gmail.com"
BOT_ID = "user_543"
USER1_MAIL = "johny.zeplin@gmail.com"
# USER1_ID = "user_542"
# LOOP_USER12_ACCESS_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1X2lkIjoiMTE3IiwiYXRfaWQiOiIxMTdfNjk1MDAzNTYtZTM1Ni1lY2NhLTNiOWMtMTg0MTkzZGYwMjJjIiwibmJmIjoxNTMzMTE0NzA1LCJleHAiOjE1MzMxMTgzMDUsImlhdCI6MTUzMzExNDcwNX0.xijzgLrAvHuuOt29cvu-XSpKY7CWP6txdxDz-K0XAmI"


# loop api functions
def get_user_id_by_email(email):
    user = get_user_by_email(email)
    if user is not None:
        return user.id


def get_chat_id(email, x_impersonate_user):
    chat = get_chat(email, x_impersonate_user)
    if chat is not None:
        return chat.id


def get_user_settings(user_id):
    setting_api = loop_api.SettingsApi()
    user = setting_api.settings_get_user_settings(x_impersonate_user=user_id, authorization=get_auth())
    return user

def upload_file(file_path, x_impersonate_user=None):
    api_instance = loop_api.FileApi()

    api_response = api_instance.file_create_file(file=file_path, authorization=get_auth(),
                                                 x_impersonate_user=x_impersonate_user)
    return api_response

#email: userja, kateremu bot posilja sporocila
def get_chat(email, x_impersonate_user):
    api = loop_api.CardApi()
    user = loop_api.User(email=email, type="User")
    integration_user = loop_api.User(email=BOT_MAIL, type="User")
    card = loop_api.CardChat(type="CardChat",
                             share_list=loop_api.ListOfResourcesOfContactBase([integration_user, user], 2, 0, 2))
    result = api.card_create_card(card, authorization=get_auth(), x_impersonate_user=x_impersonate_user)
    return result


def get_chat_by_emails(email1, email2, x_impersonate_user):
    api = loop_api.CardApi()
    user1 = loop_api.User(email=email1, type="User")
    user2 = loop_api.User(email=email2, type="User")
    card = loop_api.CardChat(type="CardChat",
                             share_list=loop_api.ListOfResourcesOfContactBase([user1, user2], 2, 0, 2))
    result = api.card_create_card(card, authorization=get_auth(), x_impersonate_user=x_impersonate_user)
    return result


def post(content, card_id, attachment_ids=None, x_impersonate_user=None, skip_bb_code_escaping=False):
    if isinstance(card_id, str):
        if "@" in card_id:  # card_id can be email address
            card_id = get_chat_id(card_id, x_impersonate_user=x_impersonate_user)
            if not card_id:
                return False

    if attachment_ids is not None and not isinstance(attachment_ids, list):
        attachment_ids = [attachment_ids]

    if attachment_ids:
        attachments = loop_api.ListOfResourcesOfFile(
            resources=[loop_api.File(id=file_id, type="File") for file_id in attachment_ids],
            size=len(attachment_ids), offset=0, total_size=len(attachment_ids))
    else:
        attachments = None

    comment_chat = loop_api.CommentChat(type="CommentChat",
                                        parent=loop_api.CardChat(id=card_id, type="CardChat"),
                                        comment=content,
                                        attachments=attachments)

    api_instance = loop_api.CommentApi()

    result = api_instance.comment_create_comment_chat(comment_chat,
                                                      x_impersonate_user=x_impersonate_user,
                                                      authorization=get_auth(),
                                                      skip_bb_code_escaping=skip_bb_code_escaping)

    return result


def get_comment(comment_id, x_impersonate_user=None):
    api = loop_api.CommentApi()
    return api.comment_get(id=comment_id, x_impersonate_user=x_impersonate_user, authorization=get_auth(),
                           html_format='text/html-stripped')


def get_comment_lis_chat(comment_id_list, x_impersonate_user=None):
    api = loop_api.CommentApi()
    return api.comment_get_list(comment_ids=comment_id_list, x_impersonate_user=x_impersonate_user, authorization=get_auth(),
                           html_format='text/html-stripped')

def get_user_by_email(email):
    user_api = loop_api.UserApi()
    user = loop_api.User(type='User', email=email)
    user_object = user_api.user_create_contact(user, authorization=get_auth())
    return user_object


def get_comments_from_chat_card(chat_card_id, offset_comments, size_comments, x_impersonate_user=BOT_ID):
    card_api = loop_api.CardApi()
    card = card_api.card_get(chat_card_id, offset_comments=offset_comments, size_comments=size_comments,
                             authorization=get_auth(), x_impersonate_user=x_impersonate_user)
    return card.comments.resources


def get_card_chat_id_list_by_user_id(offset, size, user_id=BOT_ID):
    # vrne samo CardChat idje
    card_api = loop_api.CardApi()
    card_list = card_api.card_get_list(offset, size, card_types=['CardChat'], authorization=get_auth(), x_impersonate_user=user_id)
    card_id_list = [card_list.resources[index].id for index in range(len(card_list.resources))]
    return card_id_list

token = None
def get_auth():
    if token is not None:
        return "Bearer " + token.access_token
    else:
        login()
        if token is not None:
            return "Bearer " + token.access_token


def login():
    global token
    auth_api = loop_api.AuthApi()
    auth_obj = loop_api.AuthIntegration(type="AuthIntegration",
                                        identificator="loop.user12@gmail.com", secret="dw6Li520VQQ8mniUS16R3TQ38T0gj1V1UGmX5lAxASc0NsF4oRwLTwEyV1tt0cKzQNo=")
    login_data = auth_api.auth_create_integration_auth(auth_obj)
    token = login_data.token
    return True


def refresh_token():
    global token
    token_api = loop_api.TokenApi()
    new_data = token_api.token_refresh_token(token, authorization=get_auth())
    assert isinstance(new_data, loop_api.Token)
    token = new_data



# helper za poslijanje mailov, naredi post
def send_mail(content, to_mail_list, mimeType="application/html"): # type=html or text
    if mimeType == "application/html":
        result = json.dumps(content)

    resources = '"resources": ['
    for to_mail in to_mail_list:
        resources += """{
                            "$type": "User",
                            "email": \"""" + to_mail + """\"
                         },"""
    # close resources
    resources += """]"""

    data = """{
                "$type": "CommentMail",
                "to": {
                    """ + resources + """
                },
                "body": {
                    "$type": "CommentBody",
                    "mimeType": \"""" + mimeType + """\",
                    "content": \"""" + content + """\"
                },
                "author": {
                    "$type": "User",
                    "email": \"""" + BOT_MAIL + """\"
                },
                "name": "title"
            }
"""
    # TODO change hardcoded url \
    resp = requests.post("https://clean-sprint-app.intheloop.io/api/v1/comment/mail", data=data,
                         headers={"Authorization": get_auth(), "X-Impersonate-User": BOT_ID, "Accept": "application/json",
                                  "Content-Type": "application/json"})
    print(resp.status_code)


