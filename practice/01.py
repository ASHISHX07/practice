if True:
    print("hello user, i'm front man\ni made this very easy and dumb code please don't laugh at it\n1. to get sum of two numbers enter '+'\n2. to subtract two numbers enter'-'\n3. to multiply two numbers enter '*'\n4. to divide two numbers enter'/'\n imp *please enter a valid input for results*")
while True:
    try:
        a = int(input("Enter first number: "))
        print(f"\nfirst value: {a}\n")
        break
    except ValueError:
        print("Please enter a valid integer.")


while True:
    try:
        b = int(input("Enter second number: "))
        print(f"\nfirst value: {a}\nsecond value: {b}\n")
        break
    except ValueError:
        print("Please enter a valid integer.")

while True:
    try:
        c = input("Enter the operation sign (+, -, *, /): ")
        
        if c not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operation sign!")
        
        print(f"\nfirst value: {a}\nsecond value: {b}\noperation: {c}\n")
        break
        
    except ValueError as e:
        print(e)

d = int(a+b)
e = int(a-b)
f = int(a*b)
g = int(a/b)

if c=='+':
    print(f"{a} {c} {b} = {d}\nthanks using it")
elif c=='-':
    print(f"{a} {c} {b} = {e}\nthanks using it")
elif c=='*':
    print(f"{a} {c} {b} = {f}\nthanks using it")
elif c=='/':
    print(f"{a} {c} {b} = {g}\nthanks using it")
    

