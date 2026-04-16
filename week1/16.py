# Reverse counting (n to 1)
n = int(input("Enter digit: "))
while n >= 1:
    print(n, end=" ")
    n -= 1
print()   # for new line

# Numbers divisible by 3
n = int(input("\nEnter digit: "))
i = 1
while i <= n:
    if i % 3 == 0:
        print(i, end=" ")
    i += 1
print()

# Sum of even numbers
n = int(input("\nEnter digit: "))
i = 2
total = 0
while i <= n:
    total += i
    i += 2
print("Sum of even numbers:", total)

# Loop until user enters 0
num = 1
print("\nEnter numbers (0 to stop):")
while num != 0:
    num = int(input())

# Count digits
n = int(input("\nEnter number: "))
count = 0

# handle 0 case
if n == 0:
    count = 1
else:
    while n != 0:
        n //= 10
        count += 1

print("Number of digits:", count)