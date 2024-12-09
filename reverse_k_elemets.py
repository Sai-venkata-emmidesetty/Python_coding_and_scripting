"""
Given an array arr of positive integers. Reverse every sub-array group of size k.
Note: If at any instance, k is greater or equal to the array size, then reverse the entire array. You shouldn't return any array, modify the given array in place.

Examples:
Input: k = 3, arr= [1, 2, 3, 4, 5]
Output: [3, 2, 1, 5, 4]
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
"""

def reverse_certain_part(Arrray,size,k):
    for i in range(0,size,k):
        Array[i:i+k]=reversed(Array[i:i+k])
    return Array
        
Array=[1,2,3,4,5]
size=len(Array)
k=3
print(reverse_certain_part(Array,size,k))
