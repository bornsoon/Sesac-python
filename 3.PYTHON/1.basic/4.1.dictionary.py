a = (0, 1, 2, 3, 4, 5, 6)
_, *b, _, _ = a
print(b)
print(_)

inventory = {'메로나':[300, 20], '비비빅':[400, 3], '죠소바':[250, 100]}
print(inventory)

print(inventory['메로나'][0], "원")
print(inventory['메로나'][1], "개")

inventory['월드콘']=[500, 7]
print(inventory)

icecream = inventory.keys()
print(icecream, type(icecream))
icecream = list(icecream)
print(icecream, type(icecream))

values = inventory.values()
print(values, type(values))
values = list(values)
print(icecream, type(icecream))

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(sum(icecream.values()))
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
print(type(zip(keys,vals)))
result = dict(zip(keys, vals))
print(result)