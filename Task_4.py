numbers = {
    'One' :'Один',
    'Two':'Два',
    'Three' : 'Три',
    'Four':'Четыре'
}
with open ('Text_4.txt') as file, open('new_file.txt','w') as new_file:
    lines = file.readlines()
    for line in lines:
        dannie=line.split()
        znachenija=numbers.get(dannie[0])
        new_file.write(f'{line.replace(dannie[0],znachenija)}')