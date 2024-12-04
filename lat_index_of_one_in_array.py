word=[0,0,0,1,0,1] # you have to return the last index of value 1, here you should return 5
size=len(word)
last_indices={}
for index,value in enumerate(word):
       last_indices[value]=index

print(last_indices[1])



