num1 = int(input("Enter the number 1:"))
num2 =int(input("Enter the nunber 2 :"))

max_num =  lambda x ,y : x if x>y else y
print("Largest number:",max_num(num1,num2))