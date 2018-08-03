import helper
import messages
import requests
#import queries
import time
import re
#from apscheduler.schedulers.background import BackgroundScheduler

MARVEL_TOKEN = "bUfITrzmkkWMiCSgKy0NWMsu9E0imV"
MARVEL_API_URL = "https://api.marvelapp.com/graphql/"
project_id = "3246216"

user_id = helper.get_user_id_by_email(helper.USER1_MAIL)
chat = helper.get_chat(helper.USER1_MAIL, user_id)


# scheduler = BackgroundScheduler()
# scheduler.start()
# ...
# scheduler.add_job(some_job(), 'interval', minutes=1)
# scheduler.shutdown()

# user_id = helper.get_user_id_by_email(helper.USER1_MAIL)
# print(user_id)

# chat = helper.get_chat(helper.USER1_MAIL, user_id)
# print(chat)

# parameters: user_id, screen_name, chat_id, user_id
# messages.comment_message("Ema", "Fucking for virginity", "https://www.intheloop.io/", "Poletna nebuloza", chat.id,
#                         user_id)

# parameters: user_id, screen_name, chat_id, user_id
# messages.edit_message("Špela", "Bombing for peace", "https://www.intheloop.io/", chat.id, user_id)

# parameters: user_id, screen_name, chat_id, user_id
# messages.create_message("Martina", "Drinking to end problems", "https://www.intheloop.io/", chat.id, user_id)

# post_result1 = helper.post("kr en string", chat.id, None, user_id)  # johnny -> bot
# print(post_result1)
# post_result2 = helper.post("še en string", chat.id, None, helper.BOT_ID)  # bot -> johnny
# print(post_result2)

#post_result1 = helper.post("kr en string", chat.id, None, user_id)  # johnny -> bot
#print(post_result1)
#post_result2 = helper.post("še en string", chat.id, None, helper.BOT_ID)  # bot -> johnny
#print(post_result2)


BOT_WORD = '/marvin'
PROJECT_PK_WORD = 'projectPK'
MARVEL_TOKEN_WORD = 'marvelToken'
# tkole bot dobi pogovore, v katerih je vkljucen
# ce je list v celotu napolnjen, potem ponovi za naslednjih 50, drugace si prisel cez vse
card_list_offset = 0
card_list_limit = 10
# card list bo sel zmeraj cez vse
card_id_list = helper.get_card_chat_id_list_by_user_id(card_list_offset, card_list_limit, helper.BOT_ID)
while len(card_id_list) == card_list_offset + card_list_limit:
    card_list_offset += card_list_limit
    card_id_list += helper.get_card_chat_id_list_by_user_id(card_list_offset, card_list_limit, helper.BOT_ID)

for c_id in card_id_list:
    # najprej pridobi informacijo, od katerega offseta acnes gledat sporocila
    # TODO
    offset = 0
    size = 10
    comment_list = helper.get_comments_from_chat_card(c_id, offset, size)
    while len(comment_list) == offset + size:
        offset += size
        comment_list += helper.get_comments_from_chat_card(c_id, offset, size)

    # tuki mam vsa sporocila za chat z idjem c_id
    for comment in comment_list:
        if comment.comment is not None and BOT_WORD in comment.comment: # TODO AND has_req == false
            print("sporocilo za bota")
            # check for project PK
            project_pk_list = re.findall(r"" + PROJECT_PK_WORD + "\s+\w+", comment.comment)
            if len(project_pk_list) >= 1:
                project_pk = project_pk_list[0].split()[1]
                # TODO update field in object
            else: #TODO remove
                project_pk = None
            # check for marvel token
            marvel_token_list = re.findall(r"" + MARVEL_TOKEN_WORD + "\s+\w+", comment.comment)
            if len(marvel_token_list) >= 1:
                marvel_token = marvel_token_list[0].split()[1]
                # TODO update field in object
            else: #TODO remove
                marvel_token = None

            print("Dobljene vrednosti:")
            print(project_pk)
            print(marvel_token)




