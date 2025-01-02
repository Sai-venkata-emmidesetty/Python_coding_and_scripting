#reraarange given array into two parts first part will have even numbers and second half will have odd numbers of given array in python
def re_arrange(array,right,left):  #this is the optimized function.Rearranges the array without creating new lists, saving memory.
#Space complexity: O(1).
#Time Complexity:Only a single pass through the array is needed, making it O(n) time complexity
    while left < right:
        while left < right and array[left]%2==0:
            left+=1
        while left < right and array[right]%2!=0:
            right-=1
        if left < right:
            array[left],array[right]=array[right],array[left]
    return array
array = [1, 2, 3, 4, 5, 6, 7, 8, 9] #output will be [8, 2, 6, 4, 5, 3, 7, 1, 9]
size=len(array)-1
right=size
left=0
print(re_arrange(array,right,left))


#the below function is brute force
def re_arranged(arrays):
    even_array= [X for X in arrays if X%2==0]
    odd_array=[Y for Y in arrays if Y%2!=0]
    return even_array+odd_array
arrays = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(re_arranged(arrays))

"""

even_numbers = [x for x in arr if x % 2 == 0]
x for x in arr: Iterates through each element (x) in the array (arr).
if x % 2 == 0: Filters only those elements (x) that are divisible by 2 (even numbers).
The result is a new list containing only even numbers.
For the input [1, 2, 3, 4, 5, 6, 7, 8, 9], the result of this step will be:even_numbers = [2, 4, 6, 8]

"""

"""
[<expression> for <variable> in <iterable> if <condition>]
Here’s what each part does:

<expression>: This defines the value to include in the resulting list. It can be any transformation or operation applied to the variable.
<variable>: This is the placeholder for each item in the iterable as the comprehension iterates through it.
<iterable>: The collection of items you are iterating over (in this case, arr).
<condition> (optional): A filter that determines whether the current item should be included in the result.
Explanation of [x for x in arr if x % 2 == 0]:
x for x in arr:

The first x is the value to include in the result.
The second x is the variable that represents each element in arr as we iterate through it.
if x % 2 == 0:

This is the condition that filters out the values. It ensures that only numbers that are even (x % 2 == 0) are included in the result.
Why Are There Two xs?
First x (before for): Specifies the value to add to the resulting list.
Second x (after for): Represents each element in the input iterable (arr) as it is being iterated.
Example:
Suppose arr = [1, 2, 3, 4, 5].

Iteration Process:
For each element in arr, the for x in arr assigns the current element to x.
The if condition checks if x % 2 == 0.
If the condition is True, the first x (before for) is added to the resulting list.
Step-by-Step:
x = 1: 1 % 2 != 0 → not added.
x = 2: 2 % 2 == 0 → add 2.
x = 3: 3 % 2 != 0 → not added.
x = 4: 4 % 2 == 0 → add 4.
x = 5: 5 % 2 != 0 → not added.
Result: [2, 4].

Summary:
The first x determines the value to include in the resulting list.
The second x is the loop variable, representing each element in the input list during iteration.
Both xs serve different purposes but work together to construct the final list.
"""
