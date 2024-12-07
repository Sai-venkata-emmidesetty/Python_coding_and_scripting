

array_one=[2,4,7,10]
array_two=[2,3]
new_sorted_array=[]
new_sorted_array=sorted(array_one + array_two)
new_sorted_array_size=len(new_sorted_array)
array_one_size=len(array_one)
print(new_sorted_array)

for i in range(0,new_sorted_array_size):
    if i<=array_one_size-1:
        print(new_sorted_array[i],end=" ")
    elif i==array_one_size:
        print(end="\n")
        print(new_sorted_array[i],end=" ")
    else:
        print(new_sorted_array[i],end=" ")


"""
Given two sorted arrays a[] and b[] in non-decreasing order. Merge them in sorted order without using any extra space. Modify a so that it contains the first n elements and modify b so that it contains the last m elements.

Examples: 

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4 #size of array 1 elements should be printed here like size is 4(array1) here so, 4 elemets 
7 10 #next element should be printed here in next line(size of array2)

"""