import helper
import requests
import queries

MARVEL_TOKEN = "bUfITrzmkkWMiCSgKy0NWMsu9E0imV"
MARVEL_API_URL = "https://api.marvelapp.com/graphql/"

resp = requests.post(MARVEL_API_URL, data=queries.get_comments("3246216"), headers={"Authorization":"Bearer " + MARVEL_TOKEN})
print(resp.json()['data']['project']['screens']['edges'][0]['node']['comments']['edges'][0]['node']['author']['username']
      + '  commented  "'
      + resp.json()['data']['project']['screens']['edges'][0]['node']['comments']['edges'][0]['node']['message']
      + '"')

print("test")
user_id = helper.get_user_id_by_email(helper.USER1_MAIL)
print(user_id)

chat = helper.get_chat(helper.USER1_MAIL, user_id)
#print(chat)

#post_result1 = helper.post("kr en string", chat.id, None, user_id)  # johnny -> bot
#print(post_result1)
#post_result2 = helper.post("še en string", chat.id, None, helper.BOT_ID)  # bot -> johnny
#print(post_result2)



BOT_WORD = '/marvin'
# tkole bot dobi pogovore, v katerih je vkljucen
# ce je list v celotu napolnjen, potem ponovi za naslednjih 50, drugace si prisel cez vse
card_list_offset = 0
card_list_limit = 10
card_id_list = helper.get_card_chat_id_list_by_user_id(card_list_offset, card_list_limit, helper.BOT_ID)
while len(card_id_list) == card_list_offset + card_list_limit:
    card_list_offset += card_list_limit
    card_id_list += helper.get_card_chat_id_list_by_user_id(card_list_offset, card_list_limit, helper.BOT_ID)

for c_id in card_id_list:
    offset = 0
    size = 10
    comment_list = helper.get_comments_from_chat_card(c_id, offset, size)
    while len(comment_list) == offset + size:
        offset += size
        comment_list += helper.get_comments_from_chat_card(c_id, offset, size)

    # tuki mam vsa sporocila za chat z idjem c_id
    # pogledas, kdaj je bil bot dodan in od tam filtriras ce je kak message za bota
    for comment in comment_list:
        # comment.created je datetime
        # comment.comment je string
        if comment.comment is not None and BOT_WORD in comment.comment:
            print("sporocilo za bota")




