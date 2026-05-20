'''
FizzBuzz comprehension
'''
for n in range(1,21):
    if n % 3 == 0 :
        if n% 5 ==0:
            print("Fizzbuzz")
        else:
            print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)       

fb = [
    "Fizz" if n % 3 == 0 
    else "Buzz" if n % 5 == 0 
    else n
    for n in range(1,21)]
print(fb)
