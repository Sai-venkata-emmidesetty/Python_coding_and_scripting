def remove_consecutive_elements(array):
    result=[]
    n=len(array) #n=7 and i=0,1,2,3,4,5,6
    i=0
    while i<n:
        if i<n-1 and array[i]==array[i+1]: 
            while i<n-1 and array[i]==array[i+1]:
                i+=1
        else:
            result.append(array[i])
            i+=1
    return result
array=[1,0,0,1,1,1,0] 
result=[]
print(remove_consecutive_elements(array))

"""
why did the i<n in while(outer loop) and whilw i<n-1 in inner loop
because i want the last element to check too.
"""