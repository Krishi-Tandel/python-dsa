# some programs using day 1 concepts
#Swap two variables without using a third variable. Then do it the Pythonic way (one line). Print both approaches
# using third variable
a = 3
b = 4
a,b = b,a
print("Using third variable" ,a,b)
# without using third variable
a = 6
b = 9
a = a+b
b = a-b
a = a-b
print("without using third variable", a,b)