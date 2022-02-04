def interaction(ar1,ar2):
    for i in range(0,len(ar1)):
        for j in range(0,len(ar2)):
            if ar1[i]==ar2[j]:
                print(ar2[j],end=" ")
    return print(" these are interaction values of above array : ")            



arr1=[1,3,2,4,9,7,5]
arr2=[6,8,2,5,9]
interaction(arr1,arr2)