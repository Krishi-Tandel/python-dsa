'''Even or Odd Function
Write a function check_even_odd(n) that returns the string 'Even' or 'Odd'. 
Then use a for loop to call it on every number from 1 to 20 and print: '7 → Odd'.
'''
def check_even_odd(n):
    if n % 2 == 0:
        return str(n) + " -> Even"
    else:
        return str(n) + " -> Odd"
    

for i in range(1,21):
    result = check_even_odd(i)
    print(result)
