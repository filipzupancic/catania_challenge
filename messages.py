import helper


# file contains messages that are sent when new event occurs in application
# and we want to notify a user

# sends a notification about edit on project
def edit_message(user_name, screen_name, project_link, chat_id, user_id):
    if project_link is not None:
        link = "Go to project: " + project_link
    else:
        link = ""
    message = user_name + " made changes on screen #" + screen_name + "#.\n\n" + link
    helper.post(message, chat_id, None, user_id)


# sends a notification about new comment on project
def comment_message(user_name, screen_name, project_link, comment, chat_id, user_id):
    if project_link is not None:
        link = "Go to project: " + project_link
    else:
        link = ""
    message = user_name + " added new comment on screen #" + screen_name + "#. " + "\n\n@ " + comment + " @\n\n" + link
    helper.post(message, chat_id, None, user_id)


# sends a notification that new screen was created inside the project
def create_message(user_name, screen_name, project_link, chat_id, user_id):
    if project_link is not None:
        link = "Go to project:\n" + project_link
    else:
        link = ""
    message = user_name + " created new screen #" + screen_name + "#.\n\n" + link
    helper.post(message, chat_id, None, user_id)
