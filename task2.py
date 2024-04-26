#! python3
"""
###### Task 2
Ask the user to enter a name.
Check the name against a tuple that contains a series of names to see if it is a match. Use a for loop this time instead of a single if with multiple
logical operators
(2 points)

inputs:
str name

outputs:
"That name is in the list"
"That name is not in the list"

example:
Enter a name: Grace
That name is not on the list

example:
Enter a name: Lebron
That name is on the list
"""

nameList = ("Lebron","Michale","Shaq","Dennis")
x = str(input("Name:"))
for i in nameList:
    if x in nameList:
        print(" That name is in the list")
    else:
        print(" Thant name is not in the list")
    if x=="Kobe":
        print("What can I say?")
        break

    