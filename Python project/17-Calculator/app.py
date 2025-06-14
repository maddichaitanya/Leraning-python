print("==== 🔢 Simple Calculator 🔢 ====")

while True:
    print("\nselect operation: ")

    print("1. ➕ Addition ")
    print("2. ➖ Subtraction")
    print("3. ✖️ Multiplication")
    print("4. ➗ Division")
    try:
        choice = int(input("Enter Choice (1-4): "))
        if choice not in [1, 2, 3, 4]:
            print("\nEnter choice between (1-4) only!")
            continue  # Go back to the start of the loop
        else:
            num1 = float(input("Enter Number : "))
            num2 = float(input("Enter Anotrer Number : "))
            match choice:
                case 1:
                    print(f"{num1} + {num2} = {num1+num2}")
                case 2:
                    print(f"{num1} - {num2} = {num1-num2}")
                case 3:
                    print(f"{num1} * {num2} = {num1*num2}")
                case 4:
                    print(f"{num1} % {num2} = {num1 % num2}")
                case _:
                    print("\nEnter choice between (1-4) only")
    except ValueError:
        print("\nEnter number only between (1-4) only")
    except ZeroDivisionError:
        print(f"\nZero {num1} is not divided by {num2}")
    except:
        if (choice <= 4):
            print("\nEnter number between (1-4) only")
            continue

    exit = input("\nDo You Want to Continue (y/n): ").lower()
    if not exit.startswith("y"):
        print("\nThanku For using this Simle Caluculator ")
        break

# output: - https: // app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin = share & elements = WjX689nr1HB2a2k976Galg
