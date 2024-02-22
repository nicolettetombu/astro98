def min_max(numbers):
   if not numbers:
      return None #return None for an empty list
   max_value = max(numbers)
   min_value = min(numbers)
   
   return(max_value, min_value)

#example
numbers = [3, 18, 7, 14, 5,]
print(min_max(numbers))



 
