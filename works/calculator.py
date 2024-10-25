#a full calculator
num=list(map(int,input("enter the numbers with space between two numbers:").split()))
print("1.addition\n2.subtraction\n3.multiplication\n4.division")
count=len(num)
operation=int(input("Enter what you have to do:"))
if count>1:
    if operation==1:
        print(sum(num))
    elif operation==2:
        print(diff(num))
    elif operation==3:
        print(mul(num))
    elif operation==4:
        print(div(num))
    else:
        print("invalid operation")