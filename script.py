bot_template = "BOT : {0}"
user_template = "USER : {0}"


def respond(message):

    bot_message = "I can hear you! You said: " + message

    return bot_message


def send_message(message):

    print(user_template.format(message))

    response = respond(message)

    print(bot_template.format(response))


send_message("hello")


print(respond("hello!"))
