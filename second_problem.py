T=int(input("enter the number of test cases:"))
for i in range(1,T+1):
    A_I=int(input("Give the integer of which length timely variable we have to find:"))
    if A_I%2==0:
        Output=2025*(10**(A_I-4))
    else:
        output=42025*(10**(A_I-5))    
    print("The timely variable we recived of length ",A_I ,"is",Output)
    