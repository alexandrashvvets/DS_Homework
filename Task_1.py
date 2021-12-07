def delenije(a,b):
    if b != 0:
        return a / b
    else:
        return 'znamenatel ne mozhet bit 0'

a = int(input('Vedite 1 chislo:'))
b = int(input('Vedite 2 chislo:'))
print (delenije(a,b))
