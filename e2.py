import random
llista_aleatoria = [random.randint(1, 50) for i in range(100)]
sumparells = 0
sumsenars = 0
for i in range(0, 99, 2):
    sumparells = (llista_aleatoria[i]) + sumparells
for j in range(1, 99, 2):
    sumsenars = (llista_aleatoria[j]) + sumsenars
mitjana_parells = sumparells / 50
mitjana_senars = sumsenars / 50
print(f'Mitjana posicions parelles:', mitjana_parells)
print(f'Mitjana posicions parelles:', mitjana_senars)




