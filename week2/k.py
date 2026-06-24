from collections import Counter
n = [1,2,3,2,1,4,2]
print(Counter(n))

count = {}
for i in n:
    count[i] = count.get(i,0) +1
print(count)    

student = {
    "name": "Krishi",
    "age": 20,
    "city": "Surat"
}

s = input("Enter key: ")
if s in student:
    print(student[s])
else:
    print('Key not found')    

