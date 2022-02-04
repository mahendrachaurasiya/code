n=int(input("enter the no."))
def reverse(n):
    ans=0
    while(n!=0):
       digit=n%10
       
       ans=(ans*10)+digit
       n=n//10
    return ans
print(reverse(n))
