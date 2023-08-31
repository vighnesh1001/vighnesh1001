a=int(input("enter a number"))
b=int(input("enter a number"))
c=input("enter a operator")

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else :
    print("invalid operator")