#Given two sorted arrays "A" and "B" of size "M" and "N" of distinct elements. Given a value "SUM".
#The problem is to count all pairs from both arrays whose sum is equal to "SUM"

#example : INPUT=> M=4, N=4, SUM=10, A=[1,3,5,7], B=[2,3,5,8], Output has to be 2 ->(7,3) and (5,5)

def sum_equal(A,B,A_size,SUM,pairs):
    for i in range(0,A_size):
        diff=SUM-A[i]
        if diff in B:
            pairs+=1
    return pairs

A=[1,3,5,7]
B=[2,3,5,8]
SUM=10
A_size=len(A)
pairs=0
result=sum_equal(A,B,A_size,SUM,pairs)
print(result)