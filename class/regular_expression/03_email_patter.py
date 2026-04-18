import re

email = "test@gmail.com"
pattern ="^[a-zA-z0-9_-]+@[a-zA-z]+\\.[a-zA-z]{2,4}$"

k=re.match(pattern,email)
if k is None:
    print("invalid email formate")

else:
    print("Valid formate")