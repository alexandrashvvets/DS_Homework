def func_sum(numbers, sighn):
    lis = numbers.split(' ')
    summa = 0
    for i in lis:
        if i != sighn:
            summa = summa + lis(i)
        else:
            break
    return summa


sighn = '#'
itog = 0
num_lis = input("Vvedite chisla cherez probel:")

while not sighn in num_lis:
    itog = itog + func_sum(num_lis, sighn)
    print("Summa = ", itog)