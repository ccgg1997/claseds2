#my first action

print("Hello World")
#create a file 


with open("file"".txt", "w") as file:
    for i in range(10):
        #create a file and write to it
        print("hello world4x")
        print("hello world45")
        file.write("This is line %d\n" % (i+1))