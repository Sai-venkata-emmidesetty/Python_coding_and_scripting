from collections import defaultdict
def anagrams(strs):
    defined_hashmap=defaultdict(list)
    final_output=[]
    for s in strs:
        sorted_strs=tuple(sorted(s))
        defined_hashmap[sorted_strs].append(s)
    final_output.append(defined_hashmap.values())
    return final_output


strs=["eat","tea","tan","ate","nat","bat"]
#output = [["bat"],["nat","tan"],["ate","eat","tea"]]
print(anagrams(strs))


#Keys are always imutable by default
"""
for s in strs:
        sorted_strs=sorted(s)
        defined_hashmap[sorted_strs]=s
    return defined_hashmap
#this will give an error- unhashable type: 'list'
"""
#defaultdict is a dictionary subclass. It initializes a default value (here, an empty list) for keys that are not yet in the dictionary
#defined_hashmap: This dictionary will store grouped anagrams, using sorted tuples of strings as keys.
"""
sorted(s) returns a list of characters in the string s, sorted alphabetically. For example:
If s = "eat", then sorted(s) = ['a', 'e', 't'].
tuple() converts this list to a tuple: ('a', 'e', 't').
"""

"""
Anagrams (strings with the same characters in different orders) will have the same sorted tuple key.
Example:
"eat", "tea", and "ate" all result in the key ('a', 'e', 't')
"""

#defined_hashmap[sorted_strs].append(s) groups strings by their sorted tuple keys.