import random

print(" 🎶 MUSIC RECOMMENDER  🎶 ")

# Dictionaries are used to store data values in key:value pairs.
rec = {
    "love": [" Sapphire", "Shaky", "Love me like you don", "Closer"],
    "sleep": ["Sorry", "Baby", "Night Changes", "Shape of you"],
    "broken": ["We don't talk any more", "Jo tum ", "Husn", "afsos ",],
    "rock": ["Sunny Sunny", "Blue eyes", "Beliver", "Bones"]
}

select = input(" What is your mood now : (like : love ,sleep,broken,rock)")
select.lower()

if select not in rec:
    print("Sorry , ! pleace select the correct option ")
else:
    print(
        f" Check it out : {random.choice(rec[select])}")

# output :- https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share
