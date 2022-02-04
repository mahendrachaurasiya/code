
print("Hence we find tyhe dulicaate in arrray :  ") 
arr=[34,3,54,6,4,6,43,3,2,2,]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print(arr[j])
           