def target_sum_positions(A,size,target):
    current_sum=0
    target_positions=[]
    for i in range(0,size):
        current_sum=target-A[i]
        if current_sum in A:
            target_positions.append(A.index(A[i]))
            target_positions.append(A.index(current_sum))
            break
    return target_positions


A=[2,7,11,15]
target=26
target_positions=target_sum_positions(A,len(A)-1,target)
print(target_positions[0],target_positions[1])
