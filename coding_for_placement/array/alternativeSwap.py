# def alternativeSwap(arr):
#     i=0
#     while i<len(arr)-1:
#         temp=arr[i]
#         arr[i]=arr[i+1]
#         arr[i+1]=temp
#         i+=2
#     return arr    
# by for loop 
def alternativeSwap(arr):
    for i in range(0,len(arr)-1,2):
        temp=arr[i]
        arr[i]=arr[i+1]
        arr[i+1]=temp
    return arr    


ar=[89,56,4,34,64,24,9]
print(alternativeSwap(ar))