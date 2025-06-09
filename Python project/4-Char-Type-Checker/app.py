print(" 📝 Character Type Checker 📝 ")

while True:
    try:
        text = input(" 🔤  Enter Single Character  🔤 : ")
        if len(text) == 1:
            # Input is valid, proceed with the character
            character = text
            print("  You entered:", character)
            if text.isalpha():
                print(" ↩️  You entered a letter : ", text)
            elif text.isdigit():
                print(" ↩️  You entered a number : ", text)
            else:
                print(" ↩️  You entered a Special char : ", text)
        else:
            print("Invalid input. Please enter a single character.")
    except Exception as e:
        print("An error occurred:", e)
    cont = input("\n🔁 Do you want to continue? (y/n): ").strip().lower()
    if cont != 'y':
        print("👋 Thank you for using Character Type Checker. Goodbye!")
        break

# Output Link : https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share
