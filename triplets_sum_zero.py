def find_triplets(sorted_array,size):
    for i in range(size):
        j=i+1
        k=size
        while(j<k):
            if(sorted_array[i]+sorted_array[j]+sorted_array[k]==0):
                return True
            elif(sorted_array[i]+sorted_array[j]+sorted_array[k]>0):
                k-=1
            else:
                j+=1
    return False

A_array= [0,-1,2,3,1]
#sum of trilets should be zero in an array

sorted_array=sorted(A_array)
#sorted_array=[-1,0,1,2,3]

print(find_triplets(sorted_array,len(sorted_array)-1))