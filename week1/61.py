''' Repeat Printer
Write a function repeat(text, times=3) that prints the given text times number of times
using a for loop inside the function. Call it:
With just a string (uses default 3)
With a string and custom number
With times=1
'''
def repeat(text,times=3):
    for i in range(times):
        print(text)
repeat("Hii")
repeat("Jeet",times = 2)
repeat(":)", times = 1)        