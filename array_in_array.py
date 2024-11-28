A=[1,9,2,8,0,5]
b=[5,2]
# output should be true because 5,2 are in arrray A in sequence i.e. in sequence

b_length=len(b)
positions=0
count=0
base=0
check=""
for i in range(0,b_length):
    if check!="break":
        if b[i] in A:
            print("element found")
            positions=A.index(b[i])
            print(f"{positions}")
        if positions>=base:
            count+=1
            base=positions
        else:
            check="break"
            break
    else:
        break
print(count)
if count==len(b):
    print("true")
else:
    print("false")



        



