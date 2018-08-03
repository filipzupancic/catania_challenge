import helper
from card import Card
import messages
import requests
#import queries
import time
import re

# MARVEL_API_URL = "https://api.marvelapp.com/graphql/"

# array contains objects with chat card properties
card_properties_dictionary = {}

BOT_WORD = '/marvin'
PROJECT_PK_WORD = 'projectPK'
MARVEL_TOKEN_WORD = 'marvelToken'
# tkole bot dobi pogovore, v katerih je vkljucen
# ce je list v celotu napolnjen, potem ponovi za naslednjih 50, drugace si prisel cez
while True:
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
            messages.bot_initial_message(c_id, helper.BOT_ID)

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

    # checks all records in card_properties_dictionary and send query if
    # has_required_data returns True value
    for card_id in card_properties_dictionary:
        if card_properties_dictionary[card_id].has_required_data():
            messages.edit_message("Špela", "Uspesno vpisani vsi podatki", "https://www.intheloop.io/", card_id, helper.BOT_ID)
