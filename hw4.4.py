list = [1, 1, 2, 3, 4, 4]
def remove_duplicates(list):
    seen = set()
    result = []
    for num in list:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

print(remove_duplicates(list))

# im gonna be honest i had a cs friend help me with this one
