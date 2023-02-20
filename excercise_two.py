'''Create a function that takes a list of integers, sums the even and odd numbers separately, then returns the difference between the sums of the even and odd numbers.'''

from typing import List


war_of_numbers = [44, 8, 19, 5]

def value_return(new_list: List[int]) -> List:
    even_num = []
    odd_num = []
    for num in new_list:
        if (num % 2) == 0:
            even_num.append(num)
        else:
            odd_num.append(num)

    return sum(even_num) - sum(odd_num)
            

print(value_return(war_of_numbers))