month = input('Vvedite nomer mesyatsa:')
A,B,C,D = 'zima','vesna','leto','osen'
year = {'1':A,'2':A,'3':B,'4':B,'5':B,'6':C,'7':C,'8':C,'9':D,'10':D,'11':D,'12':A}
print(year[month])

year_2=[A,A,B,B,B,C,C,C,A]
print(year_2[int(month)-1])
