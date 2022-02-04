
def binearySear(ar,key):
    start=0
    end=len(ar)-1
     # mid=start+(end-start)//2 
    mid=(start+end)//2
    while start<=end:
        if ar[mid]==key:
            return mid
        elif key>ar[mid]:
            start=mid+1
        else:
            end=mid-1
       # mid=start+(end-start)//2     
        mid=(start+end)//2
    return -1    





arr=[2,5,77,79,89,91]
# binearySear(arr,91)
print("1 is present in index",binearySear(arr,89))