with open('Task1.txt','w') as file:
    line1=input('Text:\n')
    while line1:
        file.write(f'{line1}\n')
        line1 = input('Text:\n')