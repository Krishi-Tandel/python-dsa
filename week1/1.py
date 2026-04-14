#if-else simple 
n = int(input())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and range(2,6):
    print("Not weird")
elif n % 2 == 0 and range(6,21):
    print("Weird")
elif n % 2 == 0 and n>20:
    print("not weird")         