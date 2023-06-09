while True:
    print("Menu:")
    print("1. kilometers to miles")
    print("2. miles to kilometers")
    print("3. kilograms to pounds")
    print("4. pounds to kilograms")
    print("5. celsius to fahrenheit")
    print("6. fahrenheit to celsius")
    print("7. Exit")
    choice = input("Enter a number from 1-7 = ")

    if choice == '1':
        kilometers = float(input("Enter the value of kilometers: "))
        miles = kilometers * 0.621371
        print(f"{kilometers} kilometers is equal to {miles} miles")

    elif choice == '2':
        miles = float(input("Enter the value of miles: "))
        kilometers = miles / 0.621371
        print(f"{miles} miles is equal to {kilometers} kilometers")

    elif choice == '3':
        kilograms = float(input("Enter the value of kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kilograms is equal to {pounds} pounds")

    elif choice == '4':
        pounds = float(input("Enter the value of pounds: "))
        kilograms = pounds / 2.20462
        print(f"{pounds} pounds is equal to {kilograms} kilograms")

    elif choice == '5':
        celsius = float(input("Enter the value of celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} celsius is equal to {fahrenheit} fahrenheit")

    elif choice == '6':
        fahrenheit = float(input("Enter the value of fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} fahrenheit is equal to {celsius} celsius")

    elif choice == '7':
        break

    else:
        print("Invalid input. Please choose a number from 1-7.")

    print()

print("Thank you for using the unit conversion tool!")