#Given an unsorted array and you have to find the minimun difference between any pair in an array

#example input a=[2,4,5,9,7] output should be 1, Explanation: Diff between 5 and 4 is 1
#example input a=[3,10,8,6] output should be 2, Explanation: Diff between 8 and 6 is 2

def min_difference(sorted_array,size):
     minimum_diff=float('inf')
     for i in range(1,size):
          diff=sorted_array[i]-sorted_array[i-1]
          if (diff<minimum_diff):
               minimum_diff=diff
     return minimum_diff
     
array=[3,10,8,6]
sorted_array=sorted(array)
size=len(sorted_array)-1
final_result=min_difference(sorted_array,size)
print(final_result)



""""
float('inf'): This represents positive infinity in Python.

It is a special floating-point value that is greater than any finite number.
For example: float('inf') > 1000000 is True.
Why is it used here?

The goal of the min_diff variable is to keep track of the smallest difference between any two elements in the array.
At the start, we don't know the differences yet, so we initialize min_diff to the largest possible value (infinity).
This ensures that any real difference we calculate will be smaller than min_diff, and the comparison will always update it correctly during the loop.


"""