print(" ↔️  REVERSEING THE NAME ↔️")

while True:
    name = input(" Enter Name : ")
    if not name:
        break
    reverse_name = name[::-1]  # name reverseing here
    print(f"{name} Reverseing the name : {reverse_name}")
    sel = input("\nDo you want to enter another name (y/n): ")
    if sel != "y":
        break

# output :- https://app.eraser.io/workspace/lUk2zr7D6SdyPceB6K7Q?origin=share
