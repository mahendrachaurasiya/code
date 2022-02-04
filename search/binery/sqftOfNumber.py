def sqft(n):
    s=0
    e=n
    ans=-1
    mid=(s+e)//2
  
    while s<=e:
        square=mid*mid
        if square==n:
            return mid
        elif square>n:
            ans=mid
            e=mid-1
        else:
            ans=mid
            s=mid+1
        mid=(s+e)//2
    return ans

def morePrecision(n,tempSol,precision):
    ans=tempSol
    factor=1
    for i in range(0,precision):
        factor=factor%10        
        for j in range(ans,j*j<n,j=j+factor):
            ans=j
    return ans



n=int(input())
tempSol=sqft(n)
print(morePrecision(n,tempSol,3))