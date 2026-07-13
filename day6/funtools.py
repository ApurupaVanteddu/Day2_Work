from functools import lru_cache #cache function results to improve performance
@lru_cache(maxsize=None) #unlimited cache size 
def square(num): #function definition
    return num * num
print(square(5)) #output: 25 function calling

#sorting with functools.cmp_to_key
from functools import cmp_to_key
def compare(x, y):
    return x - y
nums = [3,1,4,2]
sorted_nums = sorted(nums, key=cmp_to_key(compare))
print(sorted_nums)
