class ageerror(Exception):
    pass

try:
    age = int(input("Ente your age:"))

    if age<0:
        raise ageerror("you are not eligible") # custome exception
    
    print("You are eligible")

except ageerror as e:
    print("Error:",e)

except ValueError:
    print("Please enter a valid number")