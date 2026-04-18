# import re

# words="sun rises in east in"

# # k= re.match("sun",words)
# # k= re.search("in",words)
# # k= re.findall("s",words)
# # k= re.finditer("s",words)
# # k= re.sub("s","T",words)
# k= re.split(" ",words)
# print(k)


import re

k=re.match("h.l","hello,this is python")
k=re.findall("t.i","hblo,this oythion")
k= re.search("^hello","hello python")
k= re.search("python$","hello python")
print(k)
