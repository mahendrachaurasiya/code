def selection(arr):
    for i in range(0,len(arr)):
        minIndex=i
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                minIndex=j
        temp=arr[minIndex]
        arr[minIndex]=arr[i]
        arr[i]=temp
    return arr    


arr=[9,56,8,-1,55,-66]
print(selection(arr))