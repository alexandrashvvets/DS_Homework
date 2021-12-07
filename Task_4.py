# def my_func(x, y):
#     if x < 0:
#         return "Vvedite polozhitelnoe chislo"
#     elif y > 0 :
#         return "vvedite otritsatelnoe chislo"
#     else:
#         return x**y
# x = float(input('Vedite 1 chislo:'))
# y = int(input('Vedite 2 chislo:'))
# print (my_func(x,y))


def my_func(x, y):
    if x < 0:
        return "Vvedite polozhitelnoe chislo"
    elif y > 0 :
        return "vvedite otritsatelnoe chislo"
    else:
        rezult = 1
        for i in range (y,0):
            rezult=rezult / x
        return rezult

x = float(input('Vedite 1 chislo:'))
y = int(input('Vedite 2 chislo:'))
print (my_func(x,y))