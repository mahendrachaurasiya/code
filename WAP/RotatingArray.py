def rotatArray(arr,k):
    temp=[]
    for i in range(0,len(arr)):
        temp[(i+k)%len(arr)]==arr[i]
    return arr    
