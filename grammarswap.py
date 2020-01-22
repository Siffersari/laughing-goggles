import re


def swap_pronouns(phrase):

    phrase = re.sub('I', 'you', phrase)
    phrase = re.sub('you', 'I', phrase)

    phrase = re.sub('my', 'your', phrase)
    phrase = re.sub('your', 'my', phrase)

    return phrase


pattern = 'do you remember (.*)'

message = 'do you remember when you ate strawberries in the garden'

phrase = re.search(pattern, message).group(1)

phrase = swap_pronouns(phrase)

response = "how could I forget {}".format(phrase)


print(response)
