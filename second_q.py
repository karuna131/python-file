# a = open("second_q.txt")
# i=0
# count=0
# while i<len("second_q.txt"):
#     count+=1
#     i+=1
# print(count)
# a.close()
    


file = open("second_q.txt","r") 
Counter = 0
taxt = file.read() 
CoList = taxt.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1
          
print("This is the number of lines in the file") 
print(Counter) 