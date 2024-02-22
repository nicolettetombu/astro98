def find_max(list):
    max_value = list[0]
    for num in list:
        if num > max_value:
            max_value = num
    return max_value 

def find_min(list):
    min_value = list[0]
    for num in list:
        if num < min_value:
            min_value = num
    return min_value

#example
list = [4, 7, 18, 33, 47, 2]
print(find_max(list))
print(find_min(list)) 


