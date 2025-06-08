# Lists are used to store multiple items in a single variable.

""""List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

Python Collections (Arrays)

There are four collection data types in the Python programming language:

List :- is a collection which is ordered and changeable. Allows duplicate members.
Tuple :- is a collection which is ordered and unchangeable. Allows duplicate members.
Set :- is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary :- is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.



"""

list2 = ["apple", "banaba", "chiku", "orange"]
print(list2[0:2])

# list.reverse()
# print("in reverse : ", list)

# append() adding new value to exixting list at last index
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

list2.append("cherry")
print("After append : ", list)
print(list2.remove("apple"), "After removing apple : ", list)

# print(list.pop(3), list) pop method used to remove the index value from list

# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:

print("\nAdding apple at first index : ")
list2.insert(0, "apple")
print(list2)

# Extend List
# To append elements from another list to the current list, use the extend() method.

# Example

list1 = ["nanu", "annu", "aarush", "dugu", "rayansh", "chiku"]
list2.extend(list1)
print("\n After extend function : ", list2)

# Change Item Value
# To change the value of a specific item, refer to the index number:
list2[1] = "grapes"
print(list2)


# List Comprehension (append using loop)

print("Append using loop printing only a alphabets ")
fruits = ["apple", "banana", "cherry", "mango", "kiwi"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# sort method
fruits.sort()
print("\n After sorting ", fruits)
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)

# copy list
myliist = list2.copy()
print(myliist)

# slice(:)
thislist1 = ["apple", "banana", "cherry"]
mylist1 = thislist1[0:2]
print(mylist1)
mylist1 = thislist1[::2]
print(mylist1)


# length of list
print("\n lenght of list: ", len(list2))

# Tuples :-Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and "unchangeable".

this_tuple = ("apple", "banana", "cherry", "mango")
print(this_tuple)
print("length of tuple : ", len(this_tuple))

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# using for loop
for x in thistuple:
    print(x)

for i in range(len(this_tuple)):
    print(this_tuple[i])

# using while loop
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1

# To join two or more tuples you can use the + operator:

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


# Set :- is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print("\nThe length of list: ", len(thisset))

for i in thisset:
    print(i)
print("banana" in thisset)
print("banana" not in thisset)

# adding elements Once a set is created, you cannot change its items, but you can add new items.
thisset.add("orange")
print(thisset)

# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# To remove an item in a set, use the remove(), or the discard() method.
thisset.remove("banana")
print(thisset)

thisset.discard("papaya")
print(thisset)

# Remove a random item by using the pop() method:
thisset.pop()
print(thisset)

# The del keyword will delete the set completely:
del thisset


""""Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates."""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


