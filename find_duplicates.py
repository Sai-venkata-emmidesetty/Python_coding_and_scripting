#Program to find duplicate elements in an array

limit=int(input("enter number of elements you want to input"))
lists=[]
for i in range(0,limit):
    lists.append(int(input(f"enter element{i}")))
print(f"the entered lists is{lists}")

size=len(lists)
def find_duplicates():
    original=[]
    for i in range(0,size-1):
        if lists[i] not in original:
            original.append(lists[i])
    return original



print(find_duplicates())