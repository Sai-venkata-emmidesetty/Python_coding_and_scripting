#given an integer array nums, return true if any value is repeated twice, false if all elements are distinct.

#nums= [1,2,3,1] #output should be true

#nums=[1,2,3,4] #output should be false

def distinct_elements_finder(nums):
    hashmap_defined=set()
    for num in nums:
        if num in hashmap_defined:
            return True
        else:
            hashmap_defined.add(num)
    print(hashmap_defined)
    return False


nums=[1,2,3,1]
print(distinct_elements_finder(nums))