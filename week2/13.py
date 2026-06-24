#dict comprehension 
sq = {i : i** 2 for i in range(1,11)}
print(sq)

#class methods
#.setdefault()  if key exists in dict, method returns the associated value else returns default value
inventory = {'apple': 100 , 'orange': 50 , 'banana': 20}
inventory.setdefault('watermelon', 30)
inventory.setdefault('apple', 90) # already exists so value will not change
print(inventory.setdefault('kiwi',9)) #does not exists so it will be added to dict
print(inventory)

