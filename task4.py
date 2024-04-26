# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")
a=int(input("Enter a number less than 10:"))
for i in people:
    if a < 10:
        a in people
        print(people[a-1])
        break