with open('Task1.txt','w') as file:
    filecount=file.readlines()
    nums=0
    for num,line in enumerate(filecount):
        nums= nums + 1
        wordcount= len(line.split())
        print(f'№{num+1}-{wordcount} slov')
    print(f'{nums} strok')

