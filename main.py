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

post_result1 = helper.post("kr en string", chat.id, None, user_id)  # johnny -> bot
#print(post_result1)
post_result2 = helper.post("še en string", chat.id, None, helper.BOT_ID)  # bot -> johnny
#print(post_result2)