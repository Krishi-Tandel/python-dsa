'''
Collatz Conjecture (Medium)
Start with any positive integer n. 
Repeatedly apply: if n is even → n = n // 2, if n is odd → n = n * 3 + 1. 
Stop when n reaches 1. Use a while loop. 
Print every step and count how many steps it took.
'''
n = int(input("Enter positive integer "))
steps_count = 0
print("Integer entered: ",n)
while n != 1:
    if n % 2 == 0:
        n = n // 2
        print(n, end=" ")
        steps_count += 1

    else:
        n = n * 3 + 1
        print(n, end= " ")
        steps_count += 1
print("Total steps: ",steps_count)