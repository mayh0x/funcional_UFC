# Conte os números negativos de uma lista

def countNeg(xs):
    cont = 0
    for x in xs:
        if x < 0:
            cont += 1
    return cont

print(countNeg([1,2,3,4,5]) == 0) #True
print(countNeg([1,-1,2,-3,4]) == 2) #True
print(countNeg([2,-2]) == 1) #True
print(countNeg([1,-1]) == 1) #True
print(countNeg([1,-3,-4,3,4,-5]) == 3) #True
