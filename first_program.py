# # n=4
# # i=1
# # while(i<=n):
# #     j=1
# #     value=i
# #     while(j<=i):
# #         print(value,end=" ")
# #         value+=1
# #         j+=1
# #     print("\r")
# #     i+


# # n=4
# # i=1
# # while(i<=n):
# #     j=1
# #     value=i
# #     while(j<=i):
# #         print(value,end=" ")
# #         value -=1
# #         j+=1
# #     print("\r")
# #     i+=1


# # for i in range (65,70):
# #     # inner loop for jth columns
# #     for j in range(65,i+1):
# #         print(chr(i),end="")
        
# #     print()
# i =1
# # n=5
# # while(i<=n):
# #     j=n
# #     while(j>=i):
# #         print("*",end=" ")
# #         j -=1
# #     print("\r")
# #     i +=1

# # n=5
# # i=1
# # while(i<=n):
# #     space=i-1
# #     while(space):
# #         print(" ")
# #         space +=1
# #     j=n    
# #     while(j<=n):
# #         print("*",end=" ")
# #         j -=1
# #     print("\r")
# #     i +=1
# # n=5
# # i=1
# # while(i<=n):
# #     space=i-1
# #     while(space >0):
# #         print(" ")
# #         space +=1
# #     j=1  
# #     while(j<=n):
# #         print("*",end=" ")
# #         j +=1
# #     print("\r")
# #     i +=1

# # rows = 5
# # i = rows
# # while i >= 1:
# #     j = rows
# #     while j > i:
# #         # display space
# #         print(' ', end=' ')
# #         j -= 1
# #     k = 1
# #     while k <= i:
# #         print('*', end=' ')
# #         k += 1
# #     print()
# #     i -=

n=int(input())
i=1
while(i<=n):
    space=n-i
    while(space):
        print(" ")
        space = space-1
    j=1
    while(j<=i):
        print(j,end=" ")
        j +=1

    start=i=1
    while(start):
        print(start)
        start -=1
            
    print("\r")
    i  +=1       