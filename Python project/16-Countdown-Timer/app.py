import time

print("== ⏱️ Count Down Timer ⏱️ ==")
print(" 🌟 Count Down Timer for Your choice 🌟 ")

while True:
    try:
        seconds = int(input("\n🤔 Enter seconds to Countdown from: "))
        print(f"⏳️ Starting the countdown from {seconds} seconds ⌛ ")

        for i in range(seconds, 0, -1):
            print(f"{i} seconds remaining.....")
            time.sleep(1)
        print("\n✅ Count Down Completed ✅")

    except ValueError:
        print("Enter numbers in seconds only")

    exit = input("Do you want to play again (y/n)").lower()
    if not exit.startswith("y"):
        print(" 👋 Thanku Fro playing this game : GoodBye 👋")
        break


# output:- https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share&elements=Fv1lUdvm4QbCN1fHbty63Q
