def dublicate(a):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[j]==a[i]:
                print(a[j],end=" ")
    return a            


arr=[3,4,3,4,5,8] 
print(dublicate(arr))             
