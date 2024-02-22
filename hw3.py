# 1
def power(x,y): #raises x to the power y
    count = 1
    ans = x
    while count <y:
        ans  = ans * x
        count += 1
    return ans
    

#example 
x = 2
y = 3
print(power(x,y))


