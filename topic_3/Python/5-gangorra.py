# Retorna se uma gangorra está equilibrada ou não
# A função recebe os inteiros P_1, C_1, P_2 e C_2 respectivamente
# P_1 x C_1 for igual a P_2 x C_2 => 0
# P_1 x C_1 for maior que P_2 x C_2 => -1
# P_1 x C_1 for menor que P_2 x C_2 => 1

def gangorra(a, b, c, d):
    if a * b == c * d:
        return 0
    elif a * b > c * d:
        return -1
    else:
        return 1

print(gangorra (30, 100, 60, 50) == 0) #True
print(gangorra (40, 40, 38, 60) == 1) #True
print(gangorra (35, 80, 35, 75) == -1) #True
print(gangorra (45, 23, 96, 12) == 1) #True
print(gangorra (74, 12, 65, 48) == 1) #True
print(gangorra (78, 45, 12, 23) == -1) #True