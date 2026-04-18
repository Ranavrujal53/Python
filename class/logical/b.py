# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "* " * i)



lines = 5

for i in range(1, lines + 1):
    # Print spaces
    for k in range(lines - i):
        print(" ", end="")  # 1 space is enough

    # Print stars
    for j in range(i):
        print("*", end=" ")

    print()
