if 0==0:
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



