number=input("please input a number")
n=int(number)
if (n%2)==0:
    print("this is even")
else:
    print("this is odd")
firstID=input("please input your student ID first character")
lastID=input("please input your student ID last 8 number")
x=int(lastID)
if (x%2)==0:
    print("your student ID number is even")
else:
    print("your student ID number is odd")
    
x=str(lastID)
print("your student ID  is "+firstID+lastID)