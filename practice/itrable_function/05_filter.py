a=[34,534,3343,6587,34,464,45,3,43,4,3,46,57,809,7843,34,3]
result=filter(lambda a : a % 2 == 0,a)

result_2=filter(lambda a : a %2 != 0,a)

result_3=max(a)

result_4=min(a)

result_5=filter(lambda a : a > 1000,a)

ascending=sorted(a)

descending=sorted(a,reverse=1)

two_digit= filter(lambda a : 10<= a <=99,a)

b = list(set(a))
b.sort(reverse=1)

second_max = b[1]

b = list(set(a))
b.sort(reverse=0)

second_min = b[1]
print(b[1])


print(list(result))
print(list(result_2))
print(result_3)
print(result_4)
print(list(result_5))
print(ascending)
print(descending)
print(list(two_digit))

print(second_max)
print(second_min)
