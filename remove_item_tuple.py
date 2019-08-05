tuplex1=(1,2,3,5,6,7,9)
tup2=('a','b','c','d','r')
print("Before removing tuple:",tuplex1)
tuplex1=tuplex1[:2]+tuplex1[3:]
print(tuplex1)
print("Before removing tuple:",tup2)
list1=list(tup2)
list1.remove('d')
tup2=tuple(list1)
print(tup2)

