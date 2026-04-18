str= input("Enter the string")

print("".join(reversed(str)))

print(" ".join(str.split()[::-1]))

print(" ".join(word[::-1] for word in str.split()))

txt = ["apple","banana","cherry","cherry"]
print(txt.count("cherry"))

