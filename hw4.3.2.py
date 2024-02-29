list = []
count = 1

for i in range(5):
    row = []
    for j in range(5):
        row.append(count)
        count += 1
    list.append(row)

for i in range(5):
    for j in range(5):
        if list[i][j] % 3 == 0:
            list[i][j] = '?'
for row in list:
    print(row)


# ran into a 'nonetype' error when i put 'for i in list.append(row)' in line 11
# tried to fix by putting the if statement into the for loop; didn't work. got rid of that error but just printed a bunch of ?s before the 2D list 
# fixed it by creating a whole new for loop for the "?" statement and combining the two lists together