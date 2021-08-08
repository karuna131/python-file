# f=open("wholebasic.txt", "r")
# print(f.read())



# #Return the 5 first characters of the file:
# f=open("wholebasic.taxt", "r")
# print(f.read(50))


#Read one line of the file:
# f=open("wholebasic.txt", "r")
# print(f.readline())
# print(f.readline())



#By looping through the lines of the file, you can read the whole file, line by line:
# f=open("wholebasic.txt", "r")
# for x in f:
#     print(x)



#it is a good practice to always close the file when you are done with it.
# f=open("wholebasic.txt","r")
# print(f.readline())
# f.close()


#for create 'x',  for appending 'a', for write 'w'
# for append
# f=open("wholebasic.txt", "a")
# f.write("i am karuna and i am a student.")
# f.close()
# #after write we want to append 
# f=open("wholebasic.txt","r")
# print(f.read())


# f=open("wholebasic.txt", "x")
# f.write("wow! so cute you are.")
# f.close()
# f=open("wholebasic.txt","r")
# print(f.read())



# To delete a file, you must import the OS module, and run its os.remove() function:
# import os
# if os.path.exists("wholebasic.txt"):
#     os.remove("wholebasic.txt")
# else:
#     print("the file does not exist")




