# print(" 🖋  Text Capitalizer  🖋")

# try:
#     text = str(input(" 📝 Enter Some Text 📝 : "))
#     print("✨ 1. Upper Case"
#           "\n👀 2. Lower Case "
#           "\n😎 3. Title Case "
#           "\n🔭 4. Sentence Case "
#           "\n↔️  5. Swap Case"
#           )
#     sel = int(input(" 🕵 Select Text from 1-4 only "))
#     match sel:
#         case 1:
#             print(f"✨ converted Text ✨ :  {text.upper()}")
#         case 2:
#             print(f"👀 Your Text 👀 : {text.lower()}")
#         case 3:
#             print(f"😎  Your Text 😎 : {text.title()}")
#         case 4:
#             print(f"🔭 Your Text 🔭 : {text.capitalize()}")
#         case 5:
#             print(f"↔️ Your Text ↔️ : {text.swapcase()}")
#         case _:
#             print("❌ Enter value from 1-4 ❌")
# except TypeError:
#     print(" ❌ Invalid Format 📝 ")
# except ValueError:
#     print(" ❌ Enter value from 1-4 & String not allowed  ❌")


print(" 🖋  Text Capitalizer  🖋")

while True:
    try:
        text = str(input("\n📝 Enter Some Text 📝 : "))
        print("\n✨ 1. Upper Case"
              "\n👀 2. Lower Case"
              "\n😎 3. Title Case"
              "\n🔭 4. Sentence Case"
              "\n↔️  5. Swap Case")

        sel = int(input("🕵 Select Option (1-5) : "))

        match sel:
            case 1:
                print(f"✨ Converted Text ✨ :  {text.upper()}")
            case 2:
                print(f"👀 Your Text 👀 : {text.lower()}")
            case 3:
                print(f"😎 Your Text 😎 : {text.title()}")
            case 4:
                print(f"🔭 Your Text 🔭 : {text.capitalize()}")
            case 5:
                print(f"↔️ Your Text ↔️ : {text.swapcase()}")
                cont = input(
                    "\n🔁 Do you want to continue? (y/n): ").strip().lower()
            case _:
                print("❌ Invalid selection! Please enter a number between 1 and 5 ❌")

        cont = input("\n🔁 Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            print("👋 Thank you for using Text Capitalizer. Goodbye!")
            break

    except TypeError:
        print("❌ Invalid Format 📝")
    except ValueError:
        print("❌ Please enter a number between 1 and 5 ❌")
        cont = input("\n🔁 Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            print("👋 Thank you for using Text Capitalizer. Goodbye!")
            break


# Output Link : https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share
