result = {}
with open ('Text_5.txt') as file:
    lines = file.readlines()
    for line in lines:
        dannie = line.split()
        chas=0
        for i in dannie[1:]:
            if i !='-':
                number='0'
                for j in i:
                    if j.isdigit():
                        number=number+1
                    else:
                        break
                chas =chas+int(number)
            result.update({dannie[0].strip(':'):chas})
print(result)