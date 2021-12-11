list = [i for i in range(0, 10)]
result = []
for i in range(len(list)-1):
    if list[i] < list[i+1]:
        result.append(list[i+1])

print(list)
print(result)
