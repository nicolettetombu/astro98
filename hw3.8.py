def digital_root(integer):
    ans = 0
    while integer > 0:
        ans += (integer % 10)
        integer = integer // 10
    return ans

#example
integer = 38764
print(digital_root(integer))
