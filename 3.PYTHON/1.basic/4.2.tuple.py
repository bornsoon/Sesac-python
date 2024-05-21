t = 1,2,3,4,5,6,7,8,9,10
print(type(t))

data = tuple(range(2, 100, 2))
print( data )

temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
print(a)
print(b)
print(c)

temp_list = list(temp)
print(type(temp_list))