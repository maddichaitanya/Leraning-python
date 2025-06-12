print(" 🔤  VOWEL COUNTER  🔤  ")

while True:
    text = input("\nEnter Some Text (or q to Quit) : ")
    if text.lower() == "q":
        print("\n👋 Thank you for using VOWEL COUNTER . Goodbye! 👋 ")
        break

    vowel_count = 0

    for i in text.lower():
        if i in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
    print(f"\nThe {text} has {vowel_count} Vowels")

# Output:- https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share

# Advance Version

while True:
    text = input("\nEnter Some Text (or q to Quit) : ")
    if text.lower() == "q":
        print("\n👋 Thank you for using VOWEL COUNTER . Goodbye! 👋 ")
        break
    vowel = sum(1 for i in text.lower() if i in "aeiou")
    print(f"\nThe {text} has {vowel} Vowels")
