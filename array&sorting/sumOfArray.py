def sumOfArray(arr):
    sum=0
    for i in range(0,len(arr)):
        sum=sum+arr[i]
    return sum    


print("Enterb the number:  ")
n=int(input())
arr=[1,5,698,5]
for i in range(0,len(arr)):
    arr.append(int(input()))
print("Enter the array " ,arr)

print("Total sum of array : ",sumOfArray(arr))