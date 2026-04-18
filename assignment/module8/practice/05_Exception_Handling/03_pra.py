try:
    file=open("file1.txt","r")
    print(file.read())

except FileNotFoundError:
    print("File not found!")

finally:
    try:
        file.close()
        print("file closed")
    except:
        print("File not opened ,so not close")