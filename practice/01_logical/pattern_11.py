rows = 5
cols = 5   # width of the pattern

for i in range(rows):
    for j in range(cols):
        if j == 0 or j == cols-1 or i == j or i + j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
