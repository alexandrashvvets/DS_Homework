def zarplata(stavka,chas,pemija):
    return (stavka*chas)+pemija
a = int(input('vvedite kol-vo chasov:'))
b = int(input('vvedite stavku:'))
c = int(input('vvedite premiju:'))
print(zarplata(a,b,c))