file = open("file1.txt","r")

position = file.tell()
print("Current cursor position",position)

data = file.read(70)

position = file.tell()
print("Crusor position after reading 70 cheracter:",position)

file.close()