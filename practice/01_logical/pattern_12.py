lines = 5
stars = 1
space = lines - 1
mid = (lines // 2)

for j in range(lines):
    # Print leading spaces
    for k in range(space):
        print(" ", end="")

    # Print stars (border only)
    for i in range(stars):
        if i == 0 or i == stars - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()

    # Adjust stars and spaces
    if j < mid:
        stars += 2
        space -= 1    
    else:
        stars -= 2
        space += 1
