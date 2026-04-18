import re

text = "python is a powerful lanaguage"

word=input("enter word to match:")

result = re.match(word,text)

if result:
    print("Match found at the beginnig!")

else:
    print("No match found at the beginnig ")