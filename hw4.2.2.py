list = [3, 5, 77, 8, 11, 25, 61]
def square_list(list):
    squared_list = [i ** 2 for i in list]
    return squared_list
    
    
print(square_list(list))

#encountered error where only first number was printed squared
#tried to fix it by using a map function 
#changed it to a loop and made a new list that used the og list 

    