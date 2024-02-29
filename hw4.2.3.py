listA = list(range(1, 11))

listB = list(range(20, 31))

combined_list = listA + listB
odd_list = [num for num in combined_list if num%2 !=0]





 
        
    
# keep getting an error that says 'unsupported operand type(s) for %: 'list' and 'int'
# fixed it by combining the lists and defining it as a variable
# used  https://www.quora.com/Can-you-skip-numbers-when-printing-them-on-Python-terminal#:~:text=Yes%2C%20it%20is%20possible%20to,%3D%3D%200%3A%20%23%20Skip%20even%20numbers for help determining even vs odd numbers