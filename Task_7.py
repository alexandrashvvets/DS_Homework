import json
kompanii = {}
pcount=0
psumma=0
with open ('Text_3.txt') as file:
    lines = file.readlines()
    for line in lines:
        dannie = line.split()
        prib=float(dannie[2])-float(dannie[3])
        kompanii.update({dannie[0]:prib})
        if prib>0:
            pcount=pcount+1
            psumma=prib
avgprof=psumma/pcount
itog=[kompanii,{'avgprof':avgprof}]

with open("itog.json",'w') as file:
    json.dump(itog,file)