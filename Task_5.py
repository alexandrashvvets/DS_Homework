from functools import reduce
lip = [i for i in range(100, 1001) if i % 2 == 0]
print(list)
def my_func(el_p, el):
    return el_p * el
print(reduce(my_func, lip))
