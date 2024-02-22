def rotate_digits(n):
    #extract last digit
    last_digit = n % 10
    #remove last digit from number
    n //= 10
    #find length of number
    num_length = 0
    
