# python user inditation to define block of code not curly bracket or other symbols.

# temp = 28
# if temp > 30:
#     print("It's hot today")
# elif temp > 20:
#     print("It's nice today")
# else:
#     print("ok today's")

# checking multiple condition with logical operators
# age = int(input("Enter your age : "))
# has_licence = True

# if age >= 18 and has_licence:
#     print("you have licence")
# elif age >= 18 and not has_licence:
#     print("You dont have licence :")
# else:
#     print("not elgible : ")

# nested if Conditions

score = int(input("Enter your Score : "))

if score >= 60:
    print("pass !")
    if score >= 90:
        print("First class A")
    elif score >= 80:
        print("second class B")
    elif score >= 70:
        print("3 class C")
    else:
        print("D Grade")
else:
    print("not pass !")


# Using the "in" operator with coditionals
fruit = "apple"
if fruit in ["apple", "banana"]:
    print(f"{fruit} is present in the list")
else:
    print(f"{fruit} is not present in the list")

# Ternary operator (One-line if-else statement )

age = int(input("Enter your age : "))
status = "adult" if age >= 18 else "minor"
print(f"status : {status}")


# Comparing strings
password = "Chiku121"
if password == "Chiku121":
    print("Pass is correct")
else:
    print("worng pass")

# chaining comparisons
x = 15
if 10 < x < 20:
    print("Number is between 10 and 20")


# truthy and falsy value
user_choice = ""
if user_choice:
    print("input value is provided : ")
else:
    print("inpur value is not provided : ")
    
