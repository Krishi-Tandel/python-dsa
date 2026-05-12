#removing duplicates in a list
num = [1,2,6,7,9,6,3,3,1,9,2]
uni = []
for i in num:
    if i not in uni:
        uni.append(i)
print(uni)        