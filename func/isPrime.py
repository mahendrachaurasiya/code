def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return 0

    return 1
n=int(input())
ans=isPrime(n)  
if ans==0:
    print("not prime")
else:
    print("prime")           