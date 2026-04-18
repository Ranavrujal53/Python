# f=open("test.txt",'w')
# # f.write("Writing something....")
# f.writelines(["hello python\n","hello rana"])
# f.close()

# f=open("test.txt",'a')
# f.write("Writing something....")
# f.close()

# f=open("test.txt",'r')
# data=f.read()
# print(data)
# f.close()

# f=open("test.txt",'r')
# data=f.readlines()
# print(data)
# f.close()


# f=open("test.txt",'r')
# while True:
#     data = f.readline()
#     print(data)
#     if not data:
#         break
# f.close()

# with open("test.txt",'r') as f:
#     for line in f:
#         if "hello" in line.lower():
#             print(line.strip())

# f=open("test.txt",'r')
# for line in f:
#     if "hello" in line.lower():
#         print(line.strip())


# f=open("test.txt",'r')
# for line in f:
#     line2=line.strip()
#     print(line2," ->length",len(line2))
# f.close()

# with open("test.txt",'r') as f:
#     print(f.tell())
#     f.seek(10)
#     data = f.read()
#     print(data)
#     print(f.tell())


# mode :r,w,a,r+,w+,a+,rb,wb


# with open("home.txt",'r+') as f:
#     f.write("Write somwthing")
#     f.seek(0)
#     data=f.read()
#     print(data)


# with open("logo.png",'rb') as f:
#     data = f.read()
#     print(data)


# import json 
# d={"name":"vrujal","email":"vrujal12@gmail.com"}
# with open("data.json",'w') as f:
#     json.dump(d,f)