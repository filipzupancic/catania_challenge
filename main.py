import helper
import messages
import requests
import queries
import time
from apscheduler.schedulers.background import BackgroundScheduler

MARVEL_TOKEN = "bUfITrzmkkWMiCSgKy0NWMsu9E0imV"
MARVEL_API_URL = "https://api.marvelapp.com/graphql/"

user_id = helper.get_user_id_by_email(helper.USER1_MAIL)
chat = helper.get_chat(helper.USER1_MAIL, user_id)


# scheduler = BackgroundScheduler()
# scheduler.start()

# function sends post request to project on MarvelApp and returns editedAt timestamp
def chandler_ping():
    resp = requests.post(MARVEL_API_URL, data=queries.project_last_modified("3246216"),
                         headers={"Authorization": "Bearer " + MARVEL_TOKEN})
    return resp.json()["data"]["project"]["modifiedAt"]


old_modifiedAt = chandler_ping()
while True:
    new_modifiedAt = chandler_ping()
    print ("new_modifiedAt: " + new_modifiedAt)
    print ("old_modifiedAt: " + old_modifiedAt)

    if new_modifiedAt != old_modifiedAt:
        messages.edit_message("Špela", "Bombing for peace", "https://www.intheloop.io/", chat.id, user_id)
    old_modifiedAt = new_modifiedAt
    time.sleep(1)

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
