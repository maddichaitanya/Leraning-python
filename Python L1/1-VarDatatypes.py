print("Hello World")

# String
name = "Chiku"
# int
age = 21
# Float(decimal number )
height = 7.2
# Boolean
is_student = True

print("Hello My name is ", name, "age is", age,
      "and height", height, "and i am student ", is_student)

# lower case to uppercase
message = "hello World"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.replace("l", "L"))
# false because Python is case sensitive.so, world and World are differnt words
print("world" in message)
print(len(message))

text1 = "Hello"
text2 = "hello"

if (text1 == text2):
    print("both are same")
else:
    print("both are differnt")

# Type Conversion
age_str = "30"
age_num = int(age_str)
print(type(age_num))
print(type(age_str))

# flaot to int

fl = 3.4
ab = int(fl)
print(type(ab))
