# Write a function that takes two lists and adds the first element in the first list with the first element in the second list, 
# the second element in the first list with the second element in the second list, etc, etc. Return True if all element combinations add up to the same number. 
# Otherwise, return False.

from typing import List

list_one = [1, 2, 3, 4]
list_two = [4, 3, 2, 1]

'''v1'''

# def add_list_items(list1: List[int], list2: List[int]) ->List[int]:
#     list3=[]

#     for i in range(0,len(list1)):
#         list3.append(list1[i] + list2[i])
#     return list3

# lists_sum = add_list_items(list_one,list_two)
# print(lists_sum)

# def check_list(item_list: List[int]) -> bool:
#     if len(set(item_list)) == 1:
#         return True
#     else:
#          return False

# checked_list = check_list(lists_sum)
# print(checked_list)

'''v2'''

def add_list_items(list1: List[int], list2: List[int]) ->List[int]:
    list3=[]

    for i in range(0,len(list1)):
        list3.append(list1[i] + list2[i])
    if len(set(list3)) == 1:
        return True
    else:
        return False
    

print(add_list_items(list_one,list_two))

'''Giedriaus code'''

# from typing import List
# item_list_1 = [1, 8, 5, 0, -1, 7]
# item_list_2 = [0, -7, -4, 1, 2, -6]
# def add_puzle(item1: List[int], item2: List[int]) -> bool:
#     c = []
#     for x, y in zip(item1, item2):
#         c.append(x + y)
#     if len(set(c)) == 1:
#         return True    
#     else:
#         return False


# print(add_puzle(item_list_1, item_list_2))