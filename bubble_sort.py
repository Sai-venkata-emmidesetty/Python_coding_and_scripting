bubble=[-5,100,40,0,30,25,-1]
size=len(bubble)

for i in range(0,size-1):
    for j in range(0,size-1-i):
        if bubble[j]>bubble[j+1]:
            bubble[j],bubble[j+1]=bubble[j+1],bubble[j]

print(bubble)

# o/p= [-5, -1, 0, 25, 30, 40, 100]