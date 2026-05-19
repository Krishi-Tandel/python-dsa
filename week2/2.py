name = ['Jeet','Frenny','Dhyani','Yudhav']
hobby = ['Editing','Chrochet','Drawing','Swimming']
#using for loop
my_list = []
for n,h in zip(name,hobby):
    my_list.append((n,h))
print(my_list)   
#using list comprehension

my_list = [(n,h) for n,h in zip(name,hobby)]
print(my_list)