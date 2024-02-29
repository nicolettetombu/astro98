list = []
count = 1

for i in range(5):
    row = []
    for j in range(5):
        row.append(count)
        count += 1
    list.append(row)

for row in list:
    print(row)