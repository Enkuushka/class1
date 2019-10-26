tuple1 = ('a','b','c')
tuple2 = ('a1','b1','c1')

#temp = tuple2
#tuple2 = tuple1
#tuple1 = temp

tuple1, tuple2 = tuple2, tuple1

print(tuple1)
print(tuple2)