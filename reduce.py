from functools import reduce
a=[1,2,3,4,5]
b=[6,77,8,8,9]
h=reduce(lambda x,y:x+y,a)
print(h)
e=reduce(lambda x,y:x-y,b)
print(e)
