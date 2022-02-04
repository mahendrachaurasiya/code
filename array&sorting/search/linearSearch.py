def linearSearch(n,ser):
    for i in range(0,len(n)):
        if n[i]==ser:
            print(ser,"is present ")
            break


arr=[56,4,6,0,3,8,-1,345,3,46,6,1,435,6]
ser=int(input("enter the no you want to search: "))
linearSearch(arr,ser)