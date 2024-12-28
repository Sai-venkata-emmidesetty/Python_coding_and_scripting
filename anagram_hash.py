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

"""
sorted_strs=tuple(sorted(s))
-----------------------------
Purpose: Tuples are immutable (unchangeable) and hashable, which means they can be used as keys in dictionaries.
How it's used here:
sorted_strs = tuple(sorted(s))
The code sorts the string s to create a standardized representation of all anagrams. For example, both "eat" and "tea" will become ('a', 'e', 't') after sorting.
The tuple ('a', 'e', 't') is used as a key in the dictionary (defined_hashmap) because it represents the "signature" of an anagram group.
"""
"""
Why defaultdict?
Purpose: defaultdict simplifies handling cases where keys might not yet exist in the dictionary.
How it's used here:

defined_hashmap = defaultdict(list)
If a key does not exist in the dictionary, defaultdict will automatically create a default value (in this case, an empty list) for that key.
This eliminates the need to check if a key exists and initialize it manually, which would look like:
python code example:
if key not in hashmap:
    hashmap[key] = []
Simplifies Code: You can directly append to the list of anagrams for the key without worrying if the key exists,given below:

defined_hashmap[sorted_strs].append(s)
"""
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
