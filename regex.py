import re

pattern = "do you remember .*"

message = "do you remember when you ate strawberries in the garden"

match = re.search(pattern, message)

print(match)
