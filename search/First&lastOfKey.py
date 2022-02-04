def firstOcc(arr,key): # for start element index
    s=0
    e=len(arr)-1
    ans=-1
    mid=(s+e)//2
    while s<=e:
        if arr[mid]==key:
            ans=mid
            e=mid-1
        elif key> arr[mid]:
            s=mid+1
        elif key<arr[mid]:
            e=mid-1
        mid=(s+e)//2
    return ans    

def lastOcc(arr,key): # for last element index
    s=0
    e=len(arr)-1
    ans=-1
    mid=(s+e)//2
    while s<=e:
        if arr[mid]==key:
            ans=mid
            s=mid+1
        elif key> arr[mid]:
            s=mid+1
        elif key<arr[mid]:
            e=mid-1
        mid=(s+e)//2
    return ans 
arr=[1,2,3,3,3,3,3,4,5]
key=2
firts=firstOcc(arr,key)
last=lastOcc(arr,key)
print("firts index of element",firts,",","last element of indexies",last)
total_of_element=(last-firts)+1
print(total_of_element,"of key",key)