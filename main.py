import helper
from card import Card
import messages
import queries
import re
from loop_sdk_client.models import Group, User
import random

MARVEL_API_URL = "https://api.marvelapp.com/graphql/"
COMMENT_SIZE_FETCHING = 100
CARD_SIZE_FETCHING = 100
STATUS_MAIL_SUBJECT = "Marvin has your back"
JOKES = ["How does a computer get drunk? It takes screenshots.",
         "I just got fired from my job at the keyboard factory. They told me I wasn't putting in enough shifts.",
         "Why did the programmer quit his job? Because he didn't get arrays.",
         "Some people say the glass is half full. Some people say the glass is half empty. Engineers say the glass is twice as big as necessary.",
         "Team work is important; it helps to put the blame on someone else.",
         "I get plenty of exercise – jumping to conclusions, pushing my luck, and dodging deadlines.",
         "How do construction workers party? They raise the roof.",
         "The only thing worse than seeing something done wrong is seeing it done slowly.",
         "I have a lot of jokes about unemployed people but none of them work.",
         "No jokes for you, go to work.",
         "I would love to change the world, but they won't give me the source code."
         ]

# array contains objects with chat card properties
card_properties_dictionary = {}

# how to send mail:
# helper.send_mail("content eefekf", ["johny.zeplin@gmail.com"], mimeType="application/vnd.loop.text.plain.bbtag")

# with open('email.html', 'r') as myfile:
#     data=myfile.read().replace('\n', '')
#     helper.send_mail(data, ["johny.zeplin@gmail.com"])



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
            messages.bot_initial_message_DEMO(c_id, helper.BOT_ID)

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
                invalid_operation = True
                print("sporocilo za bota: " + comment.comment)

                information_changed = False
                project_pk_list = re.findall(r"" + messages.PROJECT_PK_WORD + "\s+\d+", comment.comment)
                if len(project_pk_list) == 1:
                    project_pk = project_pk_list[0].split()[1]
                    curr_card.change_project_pk(project_pk)
                    information_changed = True
                    invalid_operation = False
                marvel_token_list = re.findall(r"" + messages.MARVEL_TOKEN_WORD + "\s+\w+", comment.comment)
                if len(marvel_token_list) == 1:
                    marvel_token = marvel_token_list[0].split()[1]
                    curr_card.change_marvel_token(marvel_token)
                    information_changed = True
                    invalid_operation = False

                if curr_card.has_required_data() and information_changed:
                    data_valid = queries.check_user_data(MARVEL_API_URL, curr_card)
                    if data_valid == 1:
                        # request failed (probably wrong marvel token)
                        print("request failed (probably wrong marvel token)")
                        curr_card.marvel_token = None
                        messages.wrong_marvel_token_message(c_id, helper.BOT_ID)
                    elif data_valid == 2:
                        # no project found (wrong project pk)
                        print("no project found (wrong project pk)")
                        curr_card.project_pk = None
                        messages.wrong_project_number_message(c_id, helper.BOT_ID)
                    elif data_valid == 0:
                        # user data valid
                        print("user data valid")
                        messages.user_data_valid_message(c_id, helper.BOT_ID)
                    else:
                        print("Something went wrong with checking for valid information in chat.")

                # check if user wants updates on mail
                if messages.MAIL_UPDATE_WORD in comment.comment and curr_card.has_required_data():
                    invalid_operation = False
                    with open('email.html', 'r') as html_file:
                        data = html_file.read().replace('\n', '')
                        loop_card = helper.get_card_by_id(c_id)
                        mail_to_list = []
                        for resource in loop_card.share_list.resources:
                            if type(resource) is Group:
                                mail_to_list.append(resource.id)
                        # if direct message, there is no group so mail_to_list will be empty
                        if not mail_to_list:
                            for resource in loop_card.share_list.resources:
                                if type(resource) is User:
                                    mail_to_list.append(resource.email)
                            status_code = helper.send_mail("User", c_id, STATUS_MAIL_SUBJECT, data, mail_to_list)
                            if status_code == 201:
                                messages.send_message_to_chat_card("Done, check your inbox.", c_id, helper.BOT_ID)
                            else:
                                messages.send_message_to_chat_card("Ooops, something went wrong.", c_id, helper.BOT_ID)

                        else:
                            #send to group
                            status_code = helper.send_mail("Group", c_id, STATUS_MAIL_SUBJECT, data, mail_to_list)
                            if status_code == 201:
                                messages.send_message_to_chat_card("Done, check your inbox.", c_id, helper.BOT_ID)
                            else:
                                messages.send_message_to_chat_card("Ooops, something went wrong.", c_id, helper.BOT_ID)

                elif messages.MAIL_UPDATE_WORD in comment.comment and not curr_card.has_required_data():
                    invalid_operation = False
                    messages.wrong_data_message(c_id, helper.BOT_ID)

                # check if user wants to chat with marvin
                if messages.JOKE_WORD in comment.comment:
                    invalid_operation = False
                    selected_joke = random.choice(JOKES)
                    messages.send_message_to_chat_card(selected_joke, c_id, helper.BOT_ID)

                if messages.HELP_WORD in comment.comment:
                    invalid_operation = False
                    messages.bot_initial_message_DEMO(c_id, helper.BOT_ID)

                # check if user entered invalid command
                if invalid_operation:
                    messages.invalid_command_message(c_id, helper.BOT_ID)

            else:
                # message was not intended for marvin
                pass

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