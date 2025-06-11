import random

print(" FANTASY RANDOM NAME GENERATOR ")

first_name = ["Maddi", "Kanthe", "CH ", "Kanu", "Sunny", "Rohit"]
last_name = ["Chaitanya", "chiku", "Nanu",
             "Sai", "Kana", "Dancer", "singher", "sharma"]

try:
    sel = int(input("\nHow many name do you want : "))
except ValueError:
    print("\nSorry Please enter only numbers ")

for i in range(sel):
    first = random.choice(first_name)
    sec = random.choice(last_name)
    print(f"{first} {sec}")


# output :- https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share
