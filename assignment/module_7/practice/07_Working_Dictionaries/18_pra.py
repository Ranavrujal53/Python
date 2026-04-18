str = input("Enter the string:")

count = {}

for i in str:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print("Character count")
for key, value in count.items():
    print(key, ":", value)