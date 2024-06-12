list1 = [1,2,3]
list2 = ['a','b','c']

zipped = zip(list1, list2)
print(list(zipped))

list3 = [True, False, True]
zipped = zip(list1, list2, list3)
print(list(zipped))

# zip으로 묶을 때는 가장 짧은 데이터를 기준으로 묶임

keys = ['name', 'age', 'phone']
values = ['Alice', 25, '123-456-7890']

my_dicts = dict(zip(keys, values))
print(my_dicts)

values_list = [
    ['Alice', 25, '123-456-7890'],
    ['Bob', 33, '123-456-7890'],
    ['Charlie', 44, '123-456-7890'],
]

dictlist = [dict(zip(keys, values)) for values in values_list]
print(dictlist)