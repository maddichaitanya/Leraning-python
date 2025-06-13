import random

print("  🎮  Coin Flip Game  🎮 ")

while True:
    coin = input("\n🤔 Flip the Coin t=Tails amd h=Heads 🤔 : ")
    if coin != "h" and coin != "t":
        print("\n🚫 Please Enter t=Tails amd h=Heads only 🚫")
        continue  # go back to Start not to exit from loop

    flip = random.choice(["h", "t"])
    if flip == "t":
        print(f"\n🪙  Coin show  {flip} = Tails")
    else:
        print(f"\n🪙  Coin show {flip} = Heads")

    if coin == flip:
        print(" \n🏆 You Won! You Guess is Correct 🥇")
    else:
        print(" \n ❌ You Lose! Your Guess is Wrong ❌  ")

    exit = input("\n Do You Want to play again (y/n) : ")
    if exit.lower() != "y":
        print("👋 Thank you for playing Coin Flip Game . Goodbye!")
        break

# output :- https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share&elements=DuYG4dXb8ygK1xKG5lM1vg
