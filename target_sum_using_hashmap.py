def target_sum_indices(array):
    hash_map_used={}
    for num in array:
        look_up=target-num
        if look_up in array:
             hash_map_used[array.index(look_up)]=num
             hash_map_used[array.index(num)]=num
    index_values=hash_map_used.keys()
    print(f"index values that add up to target sum is:{index_values}")
    return hash_map_used

array=[1,2,8,23,3]
target=9
target_sum_indices(array)
#return target sum pairs indices
