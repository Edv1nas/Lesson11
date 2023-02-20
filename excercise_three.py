'''You are given an input array of bigrams, and an array of words. Write a function that returns True if every single bigram from this array can be found at least once in an array of words.'''
from typing import List



list1 = ["beautiful", "the", "hat"]
list2 = ["at", "be", "th", "au"]



def array_of_words(word_list: List[str], segments_list: List[str]) -> List:
    for segments in segments_list[0:4]:
        if segments not in " ".join(word_list) != True:
            return False
    return True


print(array_of_words(list1, list2))