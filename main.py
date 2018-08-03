import helper
from card import Card
import messages
import requests
#import queries
import time
import re

MARVEL_TOKEN = "bUfITrzmkkWMiCSgKy0NWMsu9E0imV"
MARVEL_API_URL = "https://api.marvelapp.com/graphql/"
project_id = "3246216"

user_id = helper.get_user_id_by_email(helper.USER1_MAIL)
chat = helper.get_chat(helper.USER1_MAIL, user_id)

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

# post_result1 = helper.post("kr en string", chat.id, None, user_id)  # johnny -> bot
# print(post_result1)
# post_result2 = helper.post("še en string", chat.id, None, helper.BOT_ID)  # bot -> johnny
# print(post_result2)


# array contains objects with chat card properties
card_properties_dictionary = {}

BOT_WORD = '/marvin'
PROJECT_PK_WORD = 'projectPK'
MARVEL_TOKEN_WORD = 'marvelToken'
# tkole bot dobi pogovore, v katerih je vkljucen
# ce je list v celotu napolnjen, potem ponovi za naslednjih 50, drugace si prisel cez
card_list_offset = 0
card_list_limit = 10
card_id_list = helper.get_card_chat_id_list_by_user_id(card_list_offset, card_list_limit, helper.BOT_ID)
while len(card_id_list) == card_list_offset + card_list_limit:
    card_list_offset += card_list_limit
    card_id_list += helper.get_card_chat_id_list_by_user_id(card_list_offset, card_list_limit, helper.BOT_ID)

for key in card_properties_dictionary:
    # checks if card_properties_dictionary has any cards
    # that no longer exist and deletes them
    if key not in card_id_list:
        del card_properties_dictionary[key]

for c_id in card_id_list:
    # checks if card_id is in card_properties_dictionary
    # if not we add value to dictionary
    if c_id not in card_properties_dictionary:
        card_properties_dictionary.update({c_id: Card(None, None, 0)})

    curr_card = card_properties_dictionary[c_id]

    if curr_card.offset_comment is not None:
        offset = curr_card.offset_comment
    else:
        offset = 0

    size = 10
    comment_list = helper.get_comments_from_chat_card(c_id, offset, size)
    while len(comment_list) == offset + size:
        offset += size
        comment_list += helper.get_comments_from_chat_card(c_id, offset, size)

    curr_card.change_offset_comment(curr_card.offset_comment + len(comment_list))

    for comment in comment_list:
        if comment.comment is not None and BOT_WORD in comment.comment:
            print("sporocilo za bota")

            project_pk_list = re.findall(r"" + PROJECT_PK_WORD + "\s+\w+", comment.comment)
            if len(project_pk_list) == 1:
                project_pk = project_pk_list[0].split()[1]
                curr_card.change_project_pk(project_pk)
            marvel_token_list = re.findall(r"" + MARVEL_TOKEN_WORD + "\s+\w+", comment.comment)
            if len(marvel_token_list) == 1:
                marvel_token = marvel_token_list[0].split()[1]
                curr_card.change_marvel_token(marvel_token)

print(card_properties_dictionary)




