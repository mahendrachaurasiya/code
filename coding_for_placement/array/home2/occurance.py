def occurance(arr):
     for i in range(0,len(arr)-1):
        count=0
        for j in range(0,len(arr)-1):
            
            if arr[i]==arr[j]:
                count+=1
        print(arr[i],count)  
 
arr=[1,2,22,2,1,1]
freq=occurance(arr) 
 
#  from collections import Counter

# def occurance(arr):
#     return Counter(arr)

# if __name__=="__main__":

#     arr=[1,2,22,2,1,1]
#     freq=occurance(arr)

#     for (key,value) in freq.items():
#         print(key,"-->",value)
# //
