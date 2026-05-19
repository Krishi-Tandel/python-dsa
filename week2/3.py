#dictionary comprehension
name = ['Jeet','Frenny','Dhyani','Yudhav']
hobby = ['Editing','Chrochet','Drawing','Swimming']

dic = {name : hobby for name,hobby in zip(name,hobby) if name != 'Frenny'}
print(dic)