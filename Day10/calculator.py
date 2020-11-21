import art
print(art.logo)

def chooseAnOperation():
    return input("Choose An Operation \n+ \n- \n* \n% \n/\n")

def calculate(x,y,oper):
    if(oper=='+'):
        return x+y
    elif(oper=='-'):
        return x-y
    elif(oper=='*'):
        return x*y
    elif(oper=='/'):
        if y==0:
            print("Can't Divide By Zero")
            return "err"
        return x*y
    elif(oper=='%'):
        if y==0:
            print("Can't Divide By Zero")
            return "err"
        return x%y
    else:
        print("Invalid Operation")
        return "err"


do_calc = 'y'
num1=float(input("Enter The First Number:\n"))
while do_calc != 'x':
    oper = chooseAnOperation()
    num2=float(input("Enter The Second Number:\n"))
    ans = calculate(num1,num2,oper)
    if ans=="err":
        do_calc='n'
    else:
        print(f"{num1} {oper} {num2} = {ans}")
        do_calc = input(f"Press 'y' to continue with {ans} or 'n' for a new calculation or 'x' to exit\n")
        
    if do_calc=='n':
        num1=float(input("Enter The First Number:\n"))
    if do_calc=='y':
        num1=ans