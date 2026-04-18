def s_marks(m1, m2, m3):
    return m1 + m2 + m3

def s_percentage(total):
    return total / 3

def s_grade(per):
    if per >= 90:
        return "A"
    elif per >= 75:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "Fail"

while True:
    print("\nGrade Management System")

    name = input("Enter the Student name: ")
    mark1 = int(input("Enter marks of sub1: "))
    mark2 = int(input("Enter marks of sub2: "))
    mark3 = int(input("Enter marks of sub3: "))

    total = s_marks(mark1, mark2, mark3)
    per = s_percentage(total)
    grade = s_grade(per)

    print("\nStudent Report")
    print("Name:", name)
    print("Total marks:", total)
    print("Percentage:", per)
    print("Grade:", grade)

    choice = input("\nDo you want to add another student? (yes/no): ")
    if choice.lower() != "yes":
        print("Program Ended. Thank you!")
        break