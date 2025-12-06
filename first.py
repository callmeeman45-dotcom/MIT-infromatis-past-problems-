    # 1st problem of eginner round MIt informatics competition 2025 Problem is to find when busy beaver reaches at the classroom
time=int(input("enter the time"))
j=time
i=0
while j>1:
    j=int(j/5)
    i=i+1
print(f"MIT^{i}")

# problem 2 of beginner round MIt informatics competition 2025 Problem is to find whether the given string is repetitive or not
string = input("input the string: ")
length = len(string)
if string[length-1]=="M":
    print("Not repetitive")
    exit()
while length > 1:    
    if string[length-1]=="M":
        string = string[0:length-1]
        length = len(string)
    if string[length-2:length] == "IT" :
        string = string[0:length-2]
        length = len(string)
    else:
        print("Not repetitive")
        break
print(string)
if string == "M":
    print("Repetitive")


       