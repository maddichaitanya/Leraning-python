print("🎨  COLOR MIXER 🎨 ")

color_mixer = {
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("blue", "green"): "teal",
    ("white", "red"): "pink",
    ("red", "green"): "brown",
}
while True:

    color1 = input("\nEnter the First Color : ").lower()
    color2 = input("Enter the Second Color : ").lower()

    mix = None

    if (color1, color2) in color_mixer:
        mix = color_mixer[(color1, color2)]
    # todo:add 1 optimization

    if mix:
        print(f"When you mic {color1} and {color2},you get : {mix}!")
    else:
        print("I don't know what those colore make when they mix.")

    # exit = input("Do you Want to Continue (y/n) : ")
    # if exit.lower() != "y":
    #     break

    # or

    if not input("\nDo you Want to Continue (y/n) : ").lower().startswith("y"):
        print("👋 Thank you for using COLOR MIXER app. Goodbye!")
        break
