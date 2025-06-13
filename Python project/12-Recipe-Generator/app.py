import random

print(" 🧑 🍜 Random Recipe Generator 🍩 ")

protines = ["Chiken", "beef", "tofu", "frish", "eggs"]
veggies = ["carrot", "mushroom", "bell peppers", "broccoli"]
carbs = ["rice", "pasta", "braed", "potatoes", "quinoa"]
methods = ["roasted", "baked", "grilled", "stir-fried", "sauteed", "plain"]
flovors = ["Sweet", "garlic", "lemon", "spicy", "herb"]
while True:
    protine = random.choice(protines)
    veggie = random.choice(veggies)
    carb = random.choice(carbs)
    method = random.choice(methods)
    flovor = random.choice(flovors)

    print(
        f"\n Your random recipe : {flovor}{method} {protine} with {veggie} and {carb}")

    choice = input("\nDo you Want to continue y/n : ")
    if choice.lower() != "y":
        print("👋 Thank you for using Random Recipe Generator . Goodbye!")
        break

# output:- https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share
