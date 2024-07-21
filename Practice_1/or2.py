num1 = int (input("enter num1\n"))
num2 = int (input("enter num2\n"))
num3 = int (input("enter num3\n"))
num4 = int (input("enter num4\n"))

if num1>num2 or num1>num3:# 1 1=1
    print("num1")
    if num2>num1 or num2>num3:#1 0 =1
        print("num2")
        if num3>num2 or num3>num4:#1 0 =1
            print("num3")
        else:
            print("num4")
