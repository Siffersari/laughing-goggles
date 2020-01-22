import re


def swap_pronouns(phrase):

    if 'I' in phrase:
        phrase = re.sub('I', 'you', phrase)

    if 'my' in phrase:
        phrase = re.sub('my', 'your', phrase)

    return phrase


print(swap_pronouns("I walk my dog"))
