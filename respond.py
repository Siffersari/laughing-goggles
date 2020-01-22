import random


def respond(message):

    if message.endswith("?"):

        return random.choice(responses["question"])

    return random.choice(responses["statement"])


send_message("what's today's weather?")
send_message("what's today's weather?")


send_message("I love building chatbots")
send_message("I love building chatbots")
