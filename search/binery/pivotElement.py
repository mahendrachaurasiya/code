def pivot(arr):
    s=0
    e=len(arr)-1
    mid=(s+e)//2
    while s<e:
        if arr[mid]>=arr[0]:
            s=mid+1
        else:
            e=mid
        mid=(s+e)//2
    return e                  


arr=[7,8,9,1,3]
print(pivot(arr))