# dict as a counter
text = 'apple','banana','orange','apple','banana','apple'
count = {}

for item in text:
    count[item] = count.get(item , 0) +1
print(count)    

fruit = 'banana'
count = {}

for ch in fruit:
    count[ch] = count.get(ch,0) +1
print(count)   

#built in counter
from collections import Counter
text = 'apple','banana','apple','banana','orange', 'apple','banana'
print(Counter(text))