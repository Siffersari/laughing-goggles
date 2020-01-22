def respond(message):

    response, phrase = match_rule(rules, message)
    if '{0}' in response:

        phrase = replace_pronouns(phrase)

        response = response.format(phrase)
    return response


send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")
