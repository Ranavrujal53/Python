lines = 5
star = lines
space = 0

for i in range(lines+1):
    # Print spaces
    for k in range(lines-i):
        print("  ", end=" ")

    # Print stars
    for i in range(2*i-1):
        print("* ", end=" ")

    print()
    star -= 1
    space += 1

# lines = 5

# for i in range(1, lines + 1):
#     # Print spaces
#     for k in range(lines - i):
#         print(" ", end="")

#     # Print stars
#     for j in range(2 * i - 1):
#         print("*", end="")

#     print()


