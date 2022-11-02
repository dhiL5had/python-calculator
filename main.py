import os
from time import sleep

def start():

    LINE_UP= '\033[1A'
    LINE_CLEAR= '\x1b[2K'

    def delay():
        print('\nProgram restarts in (10)')
        for i in range(10,0,-1):
            sleep(1)
            print(LINE_UP, end=LINE_CLEAR)
            print(f'Program restarts in ({i})')
        start()

    os.system("cls||clear")

    def add(a,b):
        sum= a + b
        answer= f"\nSum of {a} and {b} is equal to {sum}."
        print(answer)
        delay()

    def sub(a,b):
        difference= a - b
        answer= f"\nDifference of {a} and {b} is equal to {difference}."
        print(answer)
        delay()

    def mul(a,b):
        product= a * b
        answer= f"\nProduct of {a} and {b} is equal to {product}."
        print(answer)
        delay()

    def dev(a,b):
        devident= a / b
        answer= f"\nDevident of {a} and {b} is equal to {devident}."
        print(answer)
        delay()

    print('''
        --- Welcom to Calculator ---

            A. Addition
            B. Subtraction
            C. Multiplication
            D. Devision
            E. Exit

    ''')

    operation= input("Enter your choice for operation : ").lower()

    while operation not in ["a","b","c","d","e","exit"]:
        print(LINE_UP, end=LINE_CLEAR)
        operation= input("Please enter a valid choice for operation : ").lower()

    if operation in ["a"]:
        print("\n--- Addition ---\n")
        print("Enter two numbers : \n")
        a1 = int(input("1: "))
        a2 = int(input("2: "))
        add(a1, a2)
    elif operation in ["b"]:
        print("\n--- Subtraction ---\n")
        print("Enter two numbers : \n")
        b1 = int(input("1: "))
        b2 = int(input("2: "))
        sub(b1, b2)
    elif operation in ["c"]:
        print("\n--- Multiplication ---\n")
        print("Enter two numbers : \n")
        c1 = int(input("1: "))
        c2 = int(input("2: "))
        mul(c1, c2)
    elif operation in ["d"]:
        print("\n--- Devision ---\n")
        print("Enter two numbers : \n")
        d1 = int(input("1: "))
        d2 = int(input("2: "))
        dev(d1, d2)
    elif operation in ["e","exit"]:
        print("\nExiting Program. Good luck!\n")
        quit()

start()