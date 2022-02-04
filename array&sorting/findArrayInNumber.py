v=[2,4,3,1,7,11]
v.sort()
s=0
e=len(v)-1
target=10

while s<e:
    sum=v[s]+v[e]
    if(sum==target):
        print("goted",v[s],v[e])
        break
    elif(sum>target):
        e=e-1
    else:
        s=s+1    




