''' List Basics
Create a list of 5 of your favourite fruits. 
Print the first, last, and middle element using indexing.
Then print the total number of items using len().
'''
fruits = ["apple","mango","watermelon", "grapes","banana"]
print(len(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[2])
'''List Modifier
Start with numbers = [10, 20, 30, 40, 50]. Do all of these in order:

Change the second element to 99
Add 60 to the end
Insert 5 at the very beginning
Remove 30 by value

Print the list after each step.
'''
numbers = [10,20,30,40,50]
print(numbers)
numbers [1] = 99
print(numbers)
numbers.insert(5,60)
print(numbers)
numbers.insert(0,5)
print(numbers)
numbers.remove(30)
print(numbers)
'''Looping a List
Given colors = ['red', 'green', 'blue', 'yellow', 'purple'], 
use a for loop to print each color in UPPERCASE along with its index number. 
Format: 0 → RED.
'''
colors = ['red','green','blue','yellow','purple']
for index, i in enumerate(colors):
    print(f"{index} -> {i.upper()}")
