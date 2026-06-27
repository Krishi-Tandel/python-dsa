students = [("Ravi", 88), ("Priya", 91), ("Arjun", 75)]
sorted_students = sorted(students, key = lambda x : x[0])
print(sorted_students)

num = [(1,2,3), (4,5,6),(-1,-4,-8)]
s = sorted(num, key = lambda y : y[0])
print(s)

print(max(students, key = lambda x: x[1]))

# Square every number in a list (map)
nums = [2,3,4,5]
print(list(map(lambda num: num*num, nums )))

# Keep only words longer than 4 characters (filter)
animals = ['Dog','Elephant','Tiger', 'Cow','Horse']
print(list(filter(lambda word : len(word) > 4, animals)))

# Element-wise sum of two equal-length lists (map + zip)
a = [1,2,3] 
b = [4,5,6]
s = list(map(lambda x : x[0] + x[1], zip(a,b)))
print(s)
# Check if any number in a list is divisible by 7 (any)
div = [7,14,2,49,66]
print(any(d%7==0 for d in div))
# Check if all words in a list start with a capital letter (all)
words = ['harry','Hermoine','ron','ginny','George','Fred']
print(all(word[0].isupper() for word in words))