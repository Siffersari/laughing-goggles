bot_template = "BOT : {0}"
user_template = "USER : {0}"


def respond(message):

    bot_message = "I can hear you! You said: " + message

    return bot_message


print(respond("hello!"))
