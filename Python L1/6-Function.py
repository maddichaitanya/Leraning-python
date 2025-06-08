# # A function is a block of code which only runs when it is called.

# # You can pass data, known as parameters, into a function.

# # A function can return data as a result.

# In Python a function is defined using the "def" keyword:


def my_fun():  # fun declearation
    print("hello")


my_fun()  # fun call


# Function with parameters

def my_par(name):
    print("my name is : ", name)


my_par("chiku")


def fun_call(name):
    print("Hello", name, "welcome to my app")
    print("enjoy ! ")


fun_call("annu")
fun_call("nanu")


def power(base, exponent):
    return base**exponent


print(power(2, 2))
