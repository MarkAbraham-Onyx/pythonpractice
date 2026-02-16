print("Python code 2")
print("Calculator")

a=float(input("Enter a number: "))
b=float(input("Enter another number: "))

def calc(a,b):
    print("For sum enter a, difference enter s, product enter m, quotient enter q, remainder enter r ")
    opt=input("Enter the answer you want to obtain: ")
    if opt=="a" or opt=="A":
        c=a+b
        print(c)
    elif opt=="s" or opt=="S":
        c=a-b
        print(c)
    elif opt=="m" or opt=="M":
        c=a*b
        print(c)
    elif opt=="q" or opt=="Q":
        c=a/b
        print(c)
    elif opt=="r" or opt=="R":
        c=a%b
        print(c)
    else:
        print("Invalid input")
    
    print("Do you want to perform another calculation? (y/n)")
    ans=input("Enter your answer: ")
    if ans=="y" or ans=="Y":
        a=float(input("Enter a number: "))
        b=float(input("Enter another number: "))
        calc(a,b)
    elif ans=="n" or ans=="N":
        print("Thank you for using the calculator")
        return
    else:    
        print("Invalid input")

calc(a,b)

# End of code 