def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

#example
insert_string = "yo mama"
print(count_vowels(insert_string))
# output is 3
