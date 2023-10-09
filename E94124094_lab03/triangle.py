number1=int (input ("please enter a number"))
number2=int (input ("please enter a number"))
number3=int (input ("please enter a number"))
A= [number1, number2, number3]
A.sort ()
if A[0] + A[1] <= A[2]:
    print("這不能構成一個合法的三角形")
elif A[0]==A[1] and A[1]==A[2]:
    print("這是一個正三角形")
elif A[0]==A[1] and A[1]!=A[2]:
    print("這是一個等腰三角形")
elif A[0]!=A[1] and A[1]==A [2] :
    print("這是一個等腰三角形")
else:
    print("這是一個一般的三角形")