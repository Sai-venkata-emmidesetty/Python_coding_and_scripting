#program to find the most repeated elemet in array

def most_repeated_element(arr):
    if not arr: #to handle the empty array
        return None
    frequency_map={}
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    most_repeated_value=max(frequency_map,key=frequency_map.get)
    return most_repeated_value,frequency_map[most_repeated_value]
    
array=[3,4,6,3,3,4,2,9]
result,count=most_repeated_element(array)
print(f"the most repeated element in the array is {result},which is repeated {count} times")


"""
The difference between max(frequency_map, key=frequency_map.get) and max(frequency_map, key=frequency_map.get()) lies in how the key argument is being used in the max() function.

1. max(frequency_map, key=frequency_map.get)
    Explanation:

    ->frequency_map.get is a function that takes a key as input and returns the corresponding value from the dictionary frequency_map.
    ->The max() function iterates over the keys of frequency_map.
    ->For each key, it calls frequency_map.get(key) to get the value and determines the key corresponding to the maximum value.
    Correct Usage:
        ->This is the correct and standard way to use the key argument when finding the key with the maximum value in a dictionary.

2. max(frequency_map, key=frequency_map.get())
    Explanation:
    ->frequency_map.get() is called immediately, without passing any arguments.
    ->In most cases, frequency_map.get() without arguments will result in a TypeError because get() expects at least one argument (the key to look up).
    ->Even if a default value is provided (e.g., frequency_map.get(None)), it wouldn't make sense in this context because the key argument of max() expects a callable (a function) to process the elements during iteration.
    Incorrect Usage:
      ->This will raise an error or lead to unintended behavior because frequency_map.get() is not being used as a callable function in the key argument.
"""

#if input is [3, 4, 6, 3, 3, 4, 2, 9, 4], here the o/p should be [3,4] which is repeatd 3 times
def most_repeated_elements(arr):
    if not arr:  # To handle the empty array
        return None
    frequency_map = {}
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    
    # Find the maximum frequency
    max_frequency = max(frequency_map.values()) #here max_frequency will be 3
    
    # Find all elements with the maximum frequency
    most_repeated_values = []
    for key, value in frequency_map.items():
        if value == max_frequency:
            most_repeated_values.append(key)
    
    return most_repeated_values, max_frequency

# Example usage
array = [3, 4, 6, 3, 3, 4, 2, 9]
results, count = most_repeated_elements(array)
print(f"The most repeated elements in the array are {results}, each repeated {count} times.")



