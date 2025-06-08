import math

x = 20
y = 10

print(x+y)
print(x-y)
print(x % y)
print(x/y)
print(x*y)
print(x**y)

# x = x+10
x += 10
print(x)

# Single line comment

"""" Multiline comment 
 two types of comment 
"""
# String concatenation
first_name = "Maddi "
last_name = "Chaitanya"
full_name = first_name+last_name
print("Hello my name is : " + full_name + " My Firstname : " +
      first_name + " My Lastname : " + last_name)

# f Strings
print(
    f"Hello my full name is {full_name} and my first name is {first_name} and my last name is {last_name} ")


# int flore division
a = 15
b = 7
print(a/b)  # result = 2.142857142857143
print(a//b)  # result = 2


# assing multiple line var
l, n, m = 2, 3, 4
print(l, n, m)

# Swap value
l = 30
s = 10
print("value of s = ", s, "value of l", l)
l, s = s, l
print("value of s = ", s, "value of l", l)

# relaction operatoin
a = 7
b = 5
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a <= b)
print(a >= b)


# logical operation (and or not)

print("logical operation (and or not)")
y = True
z = False

print(y and z)
print(y or z)
print(not z)

print("String Slicing ")

text = "Python Programing "
print(text[5])
print(text[0:6])
print(text[7:])

print(text[::-1])  # Reversing String


# String formanting  with .format()
name = "maddi Chaitaya"
age = 21
meg1 = "My name is {} and I am {} Years lod ".format(name, age)
print(meg1)

# using placeholder
meg2 = "My name is {0} and I am {1} Years old. {0} is a nice name ".format(
    name, age)  # (0,1)

print(meg2)


# math module

print(math.pi)
print(math.sqrt(16))
print(math.pow(4, 2))
print(math.floor(4.787))  # result 4
print(math.ceil(4.787))  # result 5

pi = 3.141592653589793
print(round(pi, 2))
