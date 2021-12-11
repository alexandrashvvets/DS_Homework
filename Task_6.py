def generator1():
    a = int(input('Vvedite start number: '))
    from itertools import islice
    from itertools import count
    for i in islice(count(a), 10):
     print(i)
generator1()

def generator2():
    list = [1, 107, None, "this_list"]
    from itertools import islice
    from itertools import cycle
    for i in islice(cycle(list), 10):
     print(i)
generator2()