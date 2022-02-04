largest=0
secondLarger=0
arr=[23,2,43,46]
for i in range(0,len(arr)):
    if(arr[i]>largest):
        secondLarger=largest
        largest=arr[i]       
    elif arr[i]>secondLarger:
        secondLarger=arr[i]    

print(secondLarger)    
print(largest)    