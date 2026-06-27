#any()- returns true if any of the element is true
num = [1,2,3,4]
print(any(num))

print(any(n > 5 for n in num))

#all() - returns true only if all elements are true
print(all(num))
print(all(n > 3 for n in num))

#sum()
print(sum(num))

#min() and max() with key = 
animals = ['Dog','Elephant', 'Tiger','Cow']
print(max(animals, key = len))
print(min(animals, key = len))

marks = {
    'Jeet' : 90,
    'Krishi' : 80,
    'Bob' : 76
}
print(max(marks, key = marks.get))
print(min(marks, key = marks.get))

#len()
print(len(animals))

#reversed()
text = 'Python'
print((list(reversed(text))))

#slicing
print(text[::-1])