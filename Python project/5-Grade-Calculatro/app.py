print(" 💯 Grade calculator 💯 ")
scores = []

while True:
    try:
        score = input("🚪 Enter a test score (or Done) : ")
        if score.lower() == "done":
            print(" 👋 Goodbye 🖐")
            break
        scores.append(float(score))
        avg = sum(scores)/len(scores)
        print(f"Avergare Score : {avg:.2f}")

        if avg >= 90:
            print("Grade A")
        elif avg >= 80:
            print("Grade B")
        elif avg >= 70:
            print("Grade C")
        elif avg >= 60:
            print("Grade D")
        else:
            print("Grade E")
    except ValueError:
        print(" ❌ you Enter Invalid Grade ❌ ")

# Output Link : https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share
