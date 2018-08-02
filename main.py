import helper
import messages
import requests
import queries
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


def chandler_ping():
    resp = requests.post(MARVEL_API_URL, data=queries.screens_last_modified(project_id),
                         headers={"Authorization": "Bearer " + MARVEL_TOKEN})
    screens = resp.json()['data']['project']['screens']['edges']
    new_modifiedAt = 0
    for i in screens:
        screen_modified_time = time.mktime(time.strptime(i['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))
        if screen_modified_time > new_modifiedAt:
            new_modifiedAt = screen_modified_time
            last_modified_screen = i

    return last_modified_screen



last_modified_screen = chandler_ping()
old_modifiedAt = time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))

while True:
    last_modified_screen = chandler_ping()
    new_modifiedAt = time.mktime(time.strptime(last_modified_screen['node']['modifiedAt'], "%Y-%m-%dT%H:%M:%S+00:00"))

    if new_modifiedAt != old_modifiedAt:
        screen_id = re.findall(r"\d+", last_modified_screen['node']['uploadUrl'])[0]
        screen_url = "https://marvelapp.com/project/"+project_id+"/screen/"+screen_id+"/"
        print(last_modified_screen['node']['displayName'] + " was modified - time:" + last_modified_screen['node']['modifiedAt'])

        messages.edit_message("Somebody", last_modified_screen['node']['displayName'], screen_url, chat.id, user_id)
        old_modifiedAt = new_modifiedAt
    else:
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
