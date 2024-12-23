def fibonacci_series(limit):
    ans=[0,1]
    for i in range(2,limit+1):
        ans.append(ans[i-1]+ans[i-2])
    return ans

limit=int(input("enter the limit for the series"))
print(fibonacci_series(limit))