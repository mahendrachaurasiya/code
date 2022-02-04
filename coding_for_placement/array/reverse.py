def reverse(n):
     s=0
     e=len(n)-1
     while s<=e:
          temp=0
          temp=n[s]
          n[s]=n[e]
          n[e]=temp
          s+=1
          e-=1
     return n     


arr=[1,234567,234579,61346,806,1,3,2,6543,1234,9]
print(reverse(arr))
