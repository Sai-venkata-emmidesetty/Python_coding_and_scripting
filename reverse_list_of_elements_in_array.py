"""
input=["h","e","l","l","o"]
output : B=['o', 'l', 'l', 'e', 'h']
"""
def reverse_the_elements(A,size,reversed):
    while size>=0:
        reversed.append(A[size])
        size-=1
    return reversed


A=["h","e","l","l","o"]
size=len(A)-1
reversed=[]
print(reverse_the_elements(A,size,reversed))




