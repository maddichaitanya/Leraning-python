import random

print(" 🔤  Word Scrambler  🔤 ")

while True:
    word = input("\n Enter a word to Scrambler (Or q to quit ): ")
    if word.lower() == "q":
        print("👋 Thank you for using Word Scambler . Goodbye! 👋 ")
        break

# Hello=["H","e","l","l","o"]
    letters = list(word)
# shuffle
    random.shuffle(letters)
    print(f" Shuffle Word are : {"".join(letters)}")
