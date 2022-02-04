def factorial(n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans    
def nCr(n,r):
    num=factorial(n)
    demo=factorial(r)*factorial(n-r)
    return num//demo

answer=nCr(8,2)
print(answer)