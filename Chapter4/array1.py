import array

a = array.array('i', [1,2,3])
b = array.array('i', [4,5,6])
c = array.array('c', 'cat')
a.extend(b)
print(a)
print(b)
print(c)