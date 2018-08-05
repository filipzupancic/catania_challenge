import helper
from card import Card
import messages
import queries
import re

MARVEL_API_URL = "https://api.marvelapp.com/graphql/"
COMMENT_SIZE_FETCHING = 100
CARD_SIZE_FETCHING = 100

# array contains objects with chat card properties
card_properties_dictionary = {}


# tkole bot dobi pogovore, v katerih je vkljucen
# ce je list v celotu napolnjen, potem ponovi za naslednjih 50, drugace si prisel cez
while True:
    print("----------------  iteration start  ----------------")
    card_list_offset = 0
    card_id_list = helper.get_card_chat_id_list_by_user_id(card_list_offset, CARD_SIZE_FETCHING, helper.BOT_ID)
    while len(card_id_list) == card_list_offset + CARD_SIZE_FETCHING:
        card_list_offset += CARD_SIZE_FETCHING
        card_id_list += helper.get_card_chat_id_list_by_user_id(card_list_offset, CARD_SIZE_FETCHING, helper.BOT_ID)

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
            # check comments size in chat and set offset because we do not want to check messages that were send before
            # bot was added to chat
            offset = 0
            comment_list = helper.get_comments_from_chat_card(c_id, offset, COMMENT_SIZE_FETCHING)
            while len(comment_list) == offset + COMMENT_SIZE_FETCHING:
                offset += COMMENT_SIZE_FETCHING
                comment_list += helper.get_comments_from_chat_card(c_id, offset, COMMENT_SIZE_FETCHING)

            card_properties_dictionary[c_id].change_offset_comment(card_properties_dictionary[c_id].offset_comment + len(comment_list))
            messages.bot_initial_message(c_id, helper.BOT_ID)

        curr_card = card_properties_dictionary[c_id]

        if curr_card.offset_comment is not None:
            offset = curr_card.offset_comment
        else:
            offset = 0

        comment_list = helper.get_comments_from_chat_card(c_id, offset, COMMENT_SIZE_FETCHING)
        while len(comment_list) == offset + COMMENT_SIZE_FETCHING:
            offset += COMMENT_SIZE_FETCHING
            comment_list += helper.get_comments_from_chat_card(c_id, offset, COMMENT_SIZE_FETCHING)

        curr_card.change_offset_comment(curr_card.offset_comment + len(comment_list))

        for comment in comment_list:
            if comment.comment is not None and comment.comment.startswith(messages.BOT_WORD):
                print("sporocilo za bota: " + comment.comment)

                project_pk_list = re.findall(r"" + messages.PROJECT_PK_WORD + "\s+\d+", comment.comment)
                if len(project_pk_list) == 1:
                    project_pk = project_pk_list[0].split()[1]
                    curr_card.change_project_pk(project_pk)
                marvel_token_list = re.findall(r"" + messages.MARVEL_TOKEN_WORD + "\s+\w+", comment.comment)
                if len(marvel_token_list) == 1:
                    marvel_token = marvel_token_list[0].split()[1]
                    curr_card.change_marvel_token(marvel_token)

                if curr_card.has_required_data():
                    data_valid = queries.check_user_data(MARVEL_API_URL, curr_card)
                    if data_valid == 0:
                        # user data valid
                        print("user data valid")
                        messages.user_data_valid_message(c_id, helper.BOT_ID)
                    elif data_valid == 1:
                        # request failed (probably wrong marvel token)
                        print("request failed (probably wrong marvel token)")
                        curr_card.marvel_token = None
                        messages.wrong_marvel_token_message(c_id, helper.BOT_ID)
                    elif data_valid == 2:
                        # no project found (wrong project pk)
                        print("no project found (wrong project pk)")
                        curr_card.project_pk = None
                        messages.wrong_project_number_message(c_id, helper.BOT_ID)


    # checks all records in card_properties_dictionary and send query if
    # has_required_data returns True value
    for card_id in card_properties_dictionary:
        if card_properties_dictionary[card_id].has_required_data():
            new_screens = queries.check_for_new_screens(MARVEL_API_URL, card_properties_dictionary[card_id])

            if new_screens is not None:
                for i in new_screens:
                    new_screen = i['node']
                    print("new screen: " + new_screen['displayName'])
                    messages.create_message(new_screen['displayName'], new_screen['uploadUrl'], card_id, helper.BOT_ID) # 'uploadUrl' je pohekan

            # in case of required data check if changes were made on marvel project
            modified_screen = queries.check_if_screen_modified(MARVEL_API_URL, card_properties_dictionary[card_id])

            if modified_screen is not None:
                print("Changes made on screen " + modified_screen.displayName)
                messages.edit_message(modified_screen.displayName, modified_screen.screen_url, card_id, helper.BOT_ID)

            # CHECK FOR COMMENTS UPDATE
            new_comments, screen_name, screen_url = queries.check_for_new_comments(MARVEL_API_URL, card_properties_dictionary[card_id])

            if new_comments is not None:
                for i in new_comments:
                    new_comment = i['node']
                    print(new_comment['author']['username'] + "  commented: " + new_comment['message'])
                    messages.comment_message(new_comment['author']['username'], screen_name,
                                             screen_url, new_comment['message'], card_id, helper.BOT_ID)