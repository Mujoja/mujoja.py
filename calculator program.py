while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:",(num1 + num2))
        elif choice == '2':
            print("Result:",(num1 -num2))
        elif choice == '3':
            print("Result:",(num1 * num2))
        elif choice == '4':
            print("Result:",(num1 / num2))

        break
    else:
        print("Invalid Input")