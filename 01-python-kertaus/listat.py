numerot = [1, 2, 3, 4, 5]

parilliset = []
for numero in numerot:
    if numero % 2 == 0:
        parilliset.append(numero)

parilliset = [x for x in numerot if x % 2 == 0]

print(parilliset)

# for i in range(5):
#     print(i ** 2)

list = [1, 2, 3, 3]
sanat = list()
print(sanat)
