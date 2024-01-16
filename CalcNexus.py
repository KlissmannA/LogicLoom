def sumx(x, y): #ADD
    result = x + y
    return result


def mulx(x, y): #mul
    result = x * y
    return result


def resx(x, y): #sub
    result = x - y
    return result


def divx(x, y): #Div
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Cannot divide by 0"


def ptx(x, y): #Square2
    print("The square is 1st No.:", x ** 2)
    print("The square is 2nd No.:", y ** 2)
    return "square calculated successfully"


def sqx(x, y): #Root
    print("The square root is 1st No.:", x ** 0.5)
    print("The square root is 2nd No.:", y ** 0.5)
    return "Square root calculated successfully"


Start = 1 #game starts with 1
while Start == 1: #For infinity Loop
    print("Hello! Welcome to the online calculator")
    x = float(input("Enter an integer: "))
    y = float(input("Enter another integer: "))
    choice = int(
        input("What would you like to do?\n1- Add\n2- Multiply\n3- Subtract\n4- Divide\n5- Square\n6- Square root: \n")) #Choice
 #compare choices.
    if choice == 1:
        print(sumx(x, y))
    elif choice == 2:
        print(mulx(x, y))
    elif choice == 3:
        print(resx(x, y))
    elif choice == 4:
        print(divx(x, y))
    elif choice == 5:
        print(ptx(x, y))
    elif choice == 6:
        print(sqx(x, y))
    else:
        print("Invalid option")

    continue_playing = int(input("Do you want to continue?\n1- Yes\n2- No: \n "))

    if continue_playing == 1:
        Start = 1
    else:
        print("Thanks for using it")
        Start = 0
