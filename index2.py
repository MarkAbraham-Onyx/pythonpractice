print("Python code 2")
print("Calculator")

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

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
elif opt=="r" or opt=="R";
    c=a%b
    print(c)
else:
    print("Invalid input")
