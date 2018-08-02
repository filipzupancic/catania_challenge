import helper
import messages

print("test")
user_id = helper.get_user_id_by_email(helper.USER1_MAIL)
print(user_id)

chat = helper.get_chat(helper.USER1_MAIL, user_id)
#print(chat)

# parameters: user_id, screen_name, chat_id, user_id
messages.comment_message("Ema", "Fucking for virginity", "https://www.intheloop.io/", "Poletna nebuloza", chat.id, user_id)

# parameters: user_id, screen_name, chat_id, user_id
messages.edit_message("Špela", "Bombing for peace", "https://www.intheloop.io/", chat.id, user_id)

# parameters: user_id, screen_name, chat_id, user_id
messages.create_message("Martina", "Drinking to end problems", "https://www.intheloop.io/", chat.id, user_id)

#post_result1 = helper.post("kr en string", chat.id, None, user_id)  # johnny -> bot
#print(post_result1)
#post_result2 = helper.post("še en string", chat.id, None, helper.BOT_ID)  # bot -> johnny
#print(post_result2)