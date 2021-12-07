def user_info(name, sname, year, city, email, phone):
    return  f'{name}, {sname}, {year}, {city}, {email}, {phone}'
first = input('vvedite imya :')
sec = input('vvedite familiyu :')
third = input('vvedite god rozhdenija :')
fourth = input('vvedite gorod prozhivanija :')
fifth =input('vvedite email :')
sixth = input('vvedite telephone :')

print(user_info(name=first,sname=sec,year=third,city=fourth,email=fifth,phone=sixth))
