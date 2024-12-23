def check_anagrams(word1,word2):
    return sorted(word1)==sorted(word2)

word1=input("enter the word1 to check")
word2=input("enter the word2 to check")
print(check_anagrams(word1,word2))
#This is the usual program that everyone writes and it is nlogn becase it is using sorted which is nlogn


from collections import Counter   #this is optimizes and o(n)
def check_optimal_anagrams(word1,word2):
    counter_word3=Counter(word3)         # Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})
    counter_word4=Counter(word4)         # Counter({'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1})
    return counter_word3==counter_word4
word3=input("enter the word1 to check") # "listen"
word4=input("enter the word2 to check") # "silent"
print(check_optimal_anagrams(word1,word2))


"""

How Counter Works:
----------------------
When you pass a string to Counter, it creates a dictionary-like object where:
    1)Keys are the unique characters in the string.
    2)Values are the counts (frequencies) of those characters in the string.
Example:
----------
from collections import Counter

word = "listen"
counter_word = Counter(word)
print(counter_word)

Output:
--------
Counter({'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1})
#This means each character appears exactly once in "listen".

"""

"""
Counter("hello")  # Counts characters in the string
Counter([1, 2, 2, 3])  # Counts items in a list
Counter({"a": 3, "b": 1})  # Can initialize from a dictionary

"""

"""
counter = Counter("banana")
print(counter["a"])  # Output: 3
print(counter["b"])  # Output: 1

"""

"""
c1 = Counter("hello")
c2 = Counter("world")
print(c1 + c2)  # Merges counts: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})
print(c1 - c2)  # Subtracts counts: Counter({'l': 1, 'h': 1, 'e': 1})

"""