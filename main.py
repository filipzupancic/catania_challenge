import helper



print("test")
user_id = helper.get_user_id_by_email(helper.USER1_MAIL)
print(user_id)

chat = helper.get_chat(helper.USER1_MAIL, user_id)
#print(chat)

post_result1 = helper.post("kr en string", chat.id, None, user_id)  # johnny -> bot
#print(post_result1)
post_result2 = helper.post("še en string", chat.id, None, helper.BOT_ID)  # bot -> johnny
#print(post_result2)