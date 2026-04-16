# some simple while loop programs for practice
# numbers upto n
n = int(input())
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
# even numbers upto n
n = int(input())
i = 2
while i <= n:
    print(i, end=" ")
    i += 2

# odd numbers upto n
n = int(input())
i = 1
while i <= n:
    print(i, end=" ")
    i += 2

# sum of first n numbers
n = int(input())
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print(total)

# multiplication table
n = int(input())
i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
