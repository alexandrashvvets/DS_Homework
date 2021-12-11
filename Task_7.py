from itertools import count
from math import factorial
def generator():
    for i in count(1):
        yield factorial(i)
gen = generator()
n = 0
for j in gen:
    if n < 6:
        print(j)
        n += 1
    else:
        break