'''
Even or Odd Counter (Easy)
Ask the user for a number n. Use a for loop with range(1, n+1) 
to count how many numbers are even and how many are odd. 
Print both counts at the end using an f-string
'''
even_count = 0
odd_count = 0
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if i % 2 == 0:
        even_count+=1
    else:
        odd_count+=1
print(f"even count: {even_count} and odd count: {odd_count}")        

