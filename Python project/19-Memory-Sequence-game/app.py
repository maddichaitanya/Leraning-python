import time
import random
import os


def clear_screen():
    # user to clear the screen terminal "cls" for windows and "clear" for mack
    os.system("cls"if os.name == "nt" else "clear")


print("\n===🧠 MEMORY SQUENCE GAME 🧠===")
print("✨ Remember the sequence and type it back! ✨")
print("\nRules :")
print("- Watch as numbers appear one by one")
print("- After the sequence is shown, type it back in order")
print("- Each round adds one more number to remember")
print("- How far can you go? 🏆\n")

input("Press Enter to start...")

sequence = []
current_round = 1
game_over = False

while not game_over:
    sequence.append(random.randint(1, 9))

    clear_screen()
    print(f"\n=== Round {current_round} ===")
    print(f"Remember this squence of {len(sequence)} number: ")

    for number in sequence:
        time.sleep(0.7)
        print(f"{number}")
        time.sleep(0.7)
        clear_screen()

    print("\nNow repeat the sequence by typing each number, seperated by spaces:")
    player_answer = input("> ")

    # split method="3,6,1" => ["3","6","1"] => [3,6,1]

    try:
        player_sequence = [int(num) for num in player_answer.split()]

    except ValueError:
        print("Enter numbers only ")
        game_over = True
        continue

    if player_sequence == sequence:
        print(f"congrates! you remembred all {len(sequence)} numbers!")
        current_round += 1
        time.sleep(2)
    else:
        print(f"Game is Over! you remembred all {current_round-1} numbers!")
        print(
            f"The correct Sequence was: {"".join(str(num for num in sequence))}")
        game_over = True

    if game_over:
        play_again = input("Do You want to play again (Yes/no): ").lower()
        if play_again.startswith('y'):
            sequence = []
            current_round = 1
            game_over = False

        else:
            print("Thanku For playing the game")
