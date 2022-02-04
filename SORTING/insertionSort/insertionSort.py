def insertionSort(arr):
    for i in range(1,len(arr)):
        temp=i
        j=i-1
        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j=j-1   
        arr[j+1]=temp 
    return arr           



arr=[10,2,4,1,7,8,3]
print(insertionSort(arr))