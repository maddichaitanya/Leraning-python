# For loop
print("counting for 1 to 5 : ")
for i in range(1, 6):
    print(i)

# riverse order
print("\nin reverse counting for 1 to 5 : ")
for j in range(5, 0, -1):
    print(j)


# while loop
print("\n While loop")
count = 1
while count <= 5:
    print(count)
    count += 1

# riverse order while

print("\n While loop in riverse order")
count = 5
while count >= 1:
    print(count)
    count -= 1


# looping through list
fruits = ["apple", "banana", "orange"]
print("\nThe iteam in list are : ")
for fruit in fruits:
    print(fruit)

# looping through list in reverse order
fruits = ["apple", "banana", "orange"]
print("\nThe iteam in list are in reverse order : ")
for fruit in reversed(fruits):
    print(fruit)


# looping with enumerate
print("\nItems with index number : ")
for index, fruit in enumerate(fruits):
    print(f"{index}:{fruit}")

""""Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates."""

# dictionarypr
print("\nDictionary values")
dictionary = {
    "name ": "chiku",
    "age ": 34,
    "friends": "nanu"
}
# print(dictionary)
for key, value in dictionary.items():
    print(f"{key} : {value}")

# list comprehension(compact loop for creating lists)
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

square = [x**2 for x in range(1, 6)]
print("sauare of 1 to 5 : ", square)

# fruits = ["apple", "banana", "orange"]
# for loop with zip()
print("\nWorking of zip method")
colors = ["red", "yellow", "orange"]
print("fruits and there color : ")
for color, fruit in zip(fruits, colors):
    print(f"{color} : {fruit}")


# Braek and continue
print("\n break")
for i in range(1, 7):
    if i == 4:
        break
    print(i)

print("\n continue ")
for i in range(1, 10):
    if i % 2 == 0:
        continue  # skip even values
    print(i)


# infinate loop with break condition
print("\nInfinate loop with break condition")
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
