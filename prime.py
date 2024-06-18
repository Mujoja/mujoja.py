number = int(input("Enter a number: "))

if number > 1:
    # Check for factors
    for i in range(2, number): # i is a divisor
        if (number % i) == 0:
            print(f"{number} is not a prime number.")
            break
    else:
        print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
