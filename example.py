#my first action

print("Hello World")
#create a file 


with open("file"".txt", "w") as file:
    for i in range(10):
        #create a file and write to it
        print("hello world")
        print("hello world2")
        print("hello world3")
        file.write("This is line %d\n" % (i+1))