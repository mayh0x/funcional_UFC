# Retorne uma lista sem o primeiro nem o último elemento

def interior(xs):
    xs.pop(0) #Tira o primeiro elemento
    xs.pop() #Tira o último elemento
    return xs

print(interior ([1,2]) == [])
print(interior ([1,3,2]) == [3])
print(interior ([2,5,3,7,3]) == [5,3,7])
print(interior ([2,2,2,4]) == [2,2])
print(interior ([1,2,3,5,7,8]) == [2,3,5,7])