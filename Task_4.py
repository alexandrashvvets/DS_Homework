list = input("Vvedite spisok: ")
split_list = list.split()
for num, split_list in enumerate(split_list):
    print(f'#{num+1}-{split_list[:10]}')
