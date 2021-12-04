list_1 = input("Vvedite spisok: ")
split_list = list_1.split()
length = len(split_list)
i = 0
if length > 1:
    while i < length - 1:
        num_1 = split_list[i]
        split_list[i]=split_list[i+1]
        split_list[i+1]=num_1
        i=i+2

print(split_list)
