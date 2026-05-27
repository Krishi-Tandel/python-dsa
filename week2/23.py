import time

b_list = list(range(1000000))

b_set = set(range(1000000))

#list
start = time.time()
999999 in b_list
end = time.time()
print("List time", end - start)

#set
start = time.time()
999999 in b_set
end = time.time()

print("set time",end - start)
