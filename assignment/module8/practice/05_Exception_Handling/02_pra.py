try:

    filename=input("Enter the file name:")

    file=open(filename,"r")
    content = file.read()
    print("\nFile content:\n",content)

    num=int(input("\n Enter a number to divide by 100:"))

    result = 100/num
    print("Result:",result)


except FileNotFoundError:
    print("The file does not exits")

except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("invalid input.please enter a valid number")

finally:
    print("\n program execute successfully")