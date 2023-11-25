def main():
    # variable need not be declared first in python like other programming languages
    # They can be used directly. Variables in python are case sensitive
    a = 3
    A = 4

    print(a)
    print(A)
    print()

    # Arithmetic operation in python can be perfomed with arithmetic operators
    # and some built in function
    a = 2
    b = 3
    c = a + b
    print(c)
    d = a * b
    print(d)
    print()

    # conditional operation in python can be obtained by if else and elif(else if)
    a = 3
    b = 9

    if b % a == 0:
        print("b is divisible by a")
    elif b + 1 == 10:
        print("increment in b produces 10")
    else:
        print("you are in else block")
    print()

# Function for checking divisibility in python
# Notice indentation after the function and
# if and else statement
def checkDivisibility(a, b):
    if a % b:
        print("a is divisible by b")
    else:
        print("a is not divisible by b")

checkDivisibility(3, 4)

if __name__ == "__main__":
    main()
