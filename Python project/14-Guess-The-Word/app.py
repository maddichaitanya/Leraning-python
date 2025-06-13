import random

print("\n=== 🎮 Guess The Word  🎮 ===")
print(" ✨ Unscramble the letters to find the word!  ")

words = ["python", "coading", "game", "computer", "fun", "learn"]

while True:
    orginal_word = random.choice(words)
    lettes = list(orginal_word)
    # coverting the words in like game="g","a","m","e" => "a","m","e","g"=ameg
    random.shuffle(lettes)
    scambled = "".join(lettes)  # ameg

    print(f"\n Scambled Word: {scambled}")

    guess = input(" 🤔 What is the Word❓: ").lower()
    if guess == orginal_word:
        print(" 🎉 congrats!, You Won")
    else:
        print(f"🤞 Better Luck !, Next Time Ans:{orginal_word}")

    if not input("\nDo you want to play again (y/n) : ").lower().startswith("y"):
        print("\n Thanku For Playing this game !. Goodbye 👋")
        break

# Output:- https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share
