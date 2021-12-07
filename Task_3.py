def my_func(a,b,c):
    minimal=min(a,b,c)
    return a+b+c-minimal

a = int(input('Vedite 1 chislo:'))
b = int(input('Vedite 2 chislo:'))
c = int(input('Vedite 3 chislo:'))
print (my_func(a,b,c))

# def my_func(a,b,c):
#     if (a>b and b>c) or (b > a and a > c):
#         return sum(a,b)
#     elif (a>b and b<c) or (c>a and a>b):
#         return sum(a,c)
#     elif (b>c and c > a) or (c>b and b>a):
#         return sum(c,b)
#
# a = int(input('Vedite 1 chislo:'))
# b = int(input('Vedite 2 chislo:'))
# c = int(input('Vedite 3 chislo:'))
# x = my_func(a,b,c)
# print(x)