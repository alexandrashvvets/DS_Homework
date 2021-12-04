rate=[9,8,2,2,1]
place = int(input('Vvedite reiting:'))

ins = False
for ina, numb in enumerate(rate):
    if place > numb:
        rate.insert(ina, numb)
        ins = True
        break
if not ins:
    rate.append(place)
