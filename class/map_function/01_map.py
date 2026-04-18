# a=[10,20,30,40,50,60]
# b=[1,2,3,4,5]
# k=map(lambda x,y : x*y,a,b)
# print(list(k))


# sub = ["python","java","php","android"]
# a=map(lambda a:len(a), sub)
# print(list(a))

# l=[4,5,2,3,5,7,23,45,65,77,7,14,78,53,97]
# def odd():
#      odd_list = []
#      for i in l:
#         if i % 2 != 0:
#             odd_list.append(i)
#      return odd_list
# print(odd())

# odd = lambda l: list(filter(lambda x: x % 2 != 0, l))
# print(odd(l))


sub=["python","java","php","android"]

for i in sub:
    if i.startswith("p"):
        print(i)

for w in sub:
    if "a" in w:
        print(w)

for i in sub:
    print(i.upper())







