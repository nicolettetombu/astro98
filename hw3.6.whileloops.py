def find_max(list):
    max_value = list[0]
    i = 1
    while i < len(list):
        if list[i] > max_value:
            max_value = list[i]
        i += 1
    return max_value

def find_min(list):
    min_value = list[0]
    i = 1
    while i > len(list):
        if list[i] < min_value:
            min_value = list[i]
        i +=1
    return min_value

#example
list = [3, 7, 18, 25]
print(find_max(list))
print(find_min(list))
