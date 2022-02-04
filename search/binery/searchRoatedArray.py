def getPivot(arr):
    s=0
    e=len(arr)-1
    mid=(s+e)//2
    while (s<e):
        if arr[mid]>=arr[0]:
            s=mid+1
        else:
            e=mid
        mid=(s+e)//2
    return s      

def binearySearch(arr,s,e,k):
   
    mid=(s+e)//2
    while s<=e:
        if arr[mid]==k:
            return mid
        elif k>arr[mid]:
            s=mid+1
        else:
            e=mid-1
        mid=(s+e)//2 
    return -1                        

#if __name__=="__main":

def getPostion(arr,k):
    pivot=getPivot(arr)
    # print(pivot)
    if (arr[pivot] <=k) and (k<= len(arr)-1):
       bineary= binearySearch(arr,pivot,len(arr)-1,k)
       return bineary
    else:
        return binearySearch(arr,0,pivot-1,k)   
    
array=[3,5,7,9,1,2]
print(getPostion(array,1))