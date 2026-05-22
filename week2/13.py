#dict comprehension 
sq = {i : i** 2 for i in range(1,11)}
print(sq)

#class methods
#.setdefault()
inventory = {'apple': 100 , 'orange': 50 , 'banana': 20}
inventory.setdefault('watermelon', 30)
inventory.setdefault('apple', 90)
print(inventory.setdefault('orange'))
print(inventory)

