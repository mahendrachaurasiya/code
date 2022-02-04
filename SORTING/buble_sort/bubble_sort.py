def bubble(arr):
    flag=False
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                flag=True
        if flag==False:
            break        
    return arr            

arr=[0,6,3,9,4,1,7]
print(bubble(arr))