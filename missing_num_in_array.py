
def find_the_missing_element(final_sorted_array):
    for i in range(size):
        if i<size-1:
            if final_sorted_array[i]+1 == final_sorted_array[i+1]:
                continue
            else:
                missing_element=final_sorted_array[i]+1
    return missing_element
    

A=[8,2,4,5,3,7,1] 
#sorted_array=[1,2,3,4,5,7,8] 
#output should be 6
final_sorted_array=sorted(A)
size=len(final_sorted_array)

print(find_the_missing_element(final_sorted_array))
