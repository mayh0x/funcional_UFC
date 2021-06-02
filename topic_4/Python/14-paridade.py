# Recebe uma lista de booleanos e se o total de Trues for ímpar
# é retornado True, se não, é retornado False

def paridade(xs):
    contTrue = 0
    for x in xs:
        if x == True:
            contTrue += 1
    if contTrue % 2 != 0:
        return True
    else:    
        return False

print(paridade ([]) == False) #True
print(paridade ([True,True,False]) == False) #True
print(paridade ([True,False,True,False,True]) == True) #True
print(paridade ([False,True,False]) == True) #True