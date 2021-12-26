import random
with open ('Text_4.txt','w') as file:
    for _ in range (30):
        file.write(f'{random.randnit(0,10)}')
with open('Text_4.txt') as file:
    numbers = file.read().split()
    summa = 0
    for i in numbers:
        summa=summa+int(i)

print(summa)