# The "try" block lets you test a block of code for errors.

# The "except" block lets you handle the error.

try:
    print(x)
except:
    print("Var x is not defined")

# Many Exceptions
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

try:
    print(y)
except NameError:
    print("var y is not defined")
except:
    print("Something went wrong")

# You can use the "else" keyword to define a block of code to be executed if no errors were raised:

try:
    print("hello")
except:
    print("something went wrong ")
else:
    print("Every thing is correct")

# The "finally" block, if specified, will be executed regardless if the try block raises an error or not.

try:
    print(a)
except:
    print("var a is not defined")
finally:
    print("try and except block is excuted")

# try to open files
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.

# c = -1
# if c < 0:
#     raise Exception("Sorry, no number below zero")


# x = "hello"

# if not type(x) is int:
#     raise TypeError("Only integers are allowed")


# Example
try:
    number = int(input("Enter any number : "))
    result = 10/number
except ValueError:
    print("Enter number only")
except ZeroDivisionError:
    print(f"Zero is not divided by 10")
else:
    print(f"10 is divided by {number} and result: {result}")
finally:
    print("try and except is working properly!")
