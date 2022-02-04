def unique(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[j]==arr[i]:
                count +=1
        if count==1:
            print(arr[i],end=" ")  
    return arr              






arr=[2,4,6,5,7,3,1,2,33,33]
print(unique(arr))