num1 = int(input("enter first num:" ))

num2 = int(input("enter second num:" ))

num3 = int(input("enter third num:" ))

if num1>num2 & num1>num3:
    print(num1,"is greatest")
elif num2>num1 & num2>num3:
    print(num2,"is greatest")
else :
    print(num3,"is the greatest")
