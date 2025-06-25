try: 
    file1 = open('sample.txt','r')
    lines = file1.readlines()
    print("Reading File Contents: ")
    i=1
    for line in lines:
        print(f"Line {i}: {line}", end="")
        i+=1
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' is not found.")
