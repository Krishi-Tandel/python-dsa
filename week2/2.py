name = ['Jeet','Frenny','Dhyani','Yudhav']
hobby = ['Editing','Chrochet','Drawing','Swimming']
'''
my_list = []
for n,h in zip(name,hobby):
    my_list.append((n,h))
print(my_list)   
''' 

my_list = [(n,h) for n,h in zip(name,hobby)]
print(my_list)