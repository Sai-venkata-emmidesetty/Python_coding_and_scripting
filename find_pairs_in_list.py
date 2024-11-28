size=int(input("enter the number of elements that you want to check for number of pairs "))
lists=[]
for i in range(0,size):
    lists.append(input(f"enter element {i}:"))
print(f"your entered lists are :{lists}")

def find_count_of_each_element(lists):
    counted_numbers=[]
    original_elemets=[]
    for i in range(0,len(lists)-1):
        if lists[i] not in original_elemets:
            counted_numbers.append(lists.count(lists[i]))
            original_elemets.append(lists[i])       
    return counted_numbers

def find_number_of_pairs(counted_numbers):
    pairs=[]
    for i in range(0,len(counted_numbers)):
        pairs.append(int(counted_numbers[i]/2))
    print(pairs)
    couples=sum(pairs)
    return couples
        

counted_numbers=find_count_of_each_element(lists)
print(counted_numbers)
final_result=find_number_of_pairs(counted_numbers)
print(f"total couples in given list is : {final_result}")


