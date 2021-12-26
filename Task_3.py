with open ('Text_3.txt') as file:
    lines = file.readlines()
    workers = {}
    zarplata= 0
    for i in lines:
        c = i.split()
        workers.update ({informat[0]:float(informat[1])})
        zarplata+=float(informat[1])
srednya=zarplata/len(workers)
print(f'Srednya zp {srednya}')

for t,v in workers.items():
    if v < 2000:
        print(f"{t}:{v}")