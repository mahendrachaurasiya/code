#(1) Write code to check a String is palindrome or not?
 
# x = input("enter the string: ")
 
# w = ""
# for i in x:
#     w = i + w
 
# if (x == w):
#     print("Yes")
# else:
#     print("No")


a =input("Enter the string: ")   
b=a[-1::-1]
if(a==b):
    print("pallindrone")
else:
    print("not pallindrone")       