import random
import math
import datetime
import os
import time
import sys  # system module

# random module
# geting random number
random_numer = random.randint(1, 10)  # 1 and 10 is included
print(f"Random number is {random_numer}")

# choose a ramdom element from list
list1 = ["apple", "banana", "cherry", "fish", "orange"]
random_list1 = random.choice(list1)
print(f"Random list is {random_list1}")

# shuffle the list
random.shuffle(list1)
print(f"shuffle the list : {list1}")

# math modules
print(f"square root of 9 : {math.sqrt(9)}")
print(f"pi : {math.pi}")
print(f"power of base 2 and power 3 : {math.pow(2, 3)}")
print(f"Celing of 4.3 : {math.ceil(4.3)}")
print(f"floor of 4.8 : {math.floor(4.8)}")

# datatime module
print(f"date and time is : {datetime.datetime.now()}")
print(f"Today's data is : {datetime.date.today()}")
print(f"current year : {datetime.date.today().year}")

# OS module

print(f"Current dir is : {os.getcwd()}")
print(f"Lsit of files : {os.listdir('.')}")

# Time module
print("Waiting for 2 sec ! ")
time.sleep(2)
print("Done!")

# system module
print(f"Python version is : {sys.version}")
print(f"Platform: {sys.platform}")
