def swap ():
    file1 = input("Enter the first file name. ")
    file2 = input("Enter the second file name. ")
    file1Object = open(file1, "r")
    file2Object = open(file2, "r")

    data1 = file1Object.read()
    data2 = file2Object.read()

    file1Write = open(file1, "w")
    file2Write = open(file2, "w")

    file1Write.write(data2)
    file2Write.write(data1)
swap()