import random

print("\n=== 🎮 Welcome to the Number Geussing Game ! 🎮 ===")
print(" ✨ I am thinking of a number between 1 to 100. You have 10 attemps. 🔢!  ")

playing = True
while playing:
    secrect_number = random.randint(1, 100)
    attemps = 0
    max_attamps = 10

    game_over = False

    while attemps < max_attamps and not game_over:
        try:
            guess = int(
                input(f"🎯 Attempt {attemps+1}/{max_attamps}. Enter your gess: "))
        except ValueError:
            print("❌ please Enter a valid number")
            continue
        attemps += 1

        if guess < secrect_number:
            print("📉 Too low! Try a higher number ! ⬆️")
        elif guess > secrect_number:
            print("📈 Too High! Try a low number ! ⬇️")
        else:
            print(
                f" Congrats! you gussed the number {secrect_number} in {attemps} attmpts.")
            game_over = True

        if attemps < max_attamps and not game_over:
            print(f"⌛ You have {max_attamps-attemps} attempts left!")

    if not game_over:
        print(f"\n😭 Game Over!, The selected number was {secrect_number}")

    play_again = input("\n Do you want to play again? (y/n): ").lower()

    if play_again.startswith("y"):
        print("new game Starting...\n")
    else:
        print("GoodBye! 👋,Thanky for playing ")
        playing = False

# Output:- https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share&elements=CM-Ipq0_tYwFBVeESHuh-g
