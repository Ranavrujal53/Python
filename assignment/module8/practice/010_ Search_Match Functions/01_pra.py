import re

text = "python is a powerful programming lanaguage"

word = input("Enter word to search:")

result= re.search(word,text)

if result:
    print("Word found")
    print("Found at position:",result.start())

else:
    print("word not found!")