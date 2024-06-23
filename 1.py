import copy
# def solution(n, edge):
#     count = 0

edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def isElement(n, edge):
    next = []
    edge1 = copy.deepcopy(edge)

    for i in edge:
        if i[0] == n:
            next.append(i[1])
            edge1.remove(i)
        elif i[1] == n:
            next.append(i[0])
            edge1.remove(i)
    
    edge = edge1
    print(edge)

    return next

next = isElement(1, edge)
print(next)

for i in next:
    for j in isElement(i, edge):
        if j not in next:
            print(j)
        


# solution(6, edge)  