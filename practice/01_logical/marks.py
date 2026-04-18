marks=int(input("Enter the marks of Student:"))

if marks>=91 and marks<=100:
    print("Grade A")
elif marks>=71 and marks<=90:
    print("Grade B")
elif marks>=51 and marks<=70:
    print("Grade C")
elif marks>=35 and marks<=50:
    print("Grade D")
elif marks>=0 and marks<=34:
    print("The studet is fail")
else:
    print("in valide number")