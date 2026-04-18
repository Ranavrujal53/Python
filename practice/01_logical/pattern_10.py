n = 7   # width of the pattern

for i in range(5):
    for j in range(n):
        if j == 0 or j == n-1 or (i == 1 and j in [2, 5]) or (i == 2 and j ==3) or (i == 3 and j in [2, 5]):
            print("*", end="")
        else:
            print(" ", end="")
    print()
