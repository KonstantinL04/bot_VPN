def get_user_name(message):
    return message.from_user.first_name

def get_user_id(message):
    return message.from_user.id

