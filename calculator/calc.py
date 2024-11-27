while True:
    try:
        num1 = float(input("Enter a number1: "))
        num2 = float(input("Enter a number2: "))
        choice = input("Enter operation (+, -, *, /): ")

        if choice == '+':
          print("sum = ", num1 + num2)
        elif choice == '-':
            print("difference = ", num1 - num2)
        elif choice == '*':
            print("product = ", num1 * num2)
        elif choice == '/':
            print("quotient = ", num1 / num2)
        else:
            print("Invalid operation")

        print("Do you want to perform another operation?")
        response = input("Enter 'yes' or 'no': ")
        if response.lower() != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter a number")

