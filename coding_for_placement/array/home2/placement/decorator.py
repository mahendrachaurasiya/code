# def decor(num):
#     def inner():
#         a=num()
#         add=a+5
#         return add
#     return inner    




# def num():
#     return 10

# result_fun=decor(num)
# print(result_fun())  


def decor(num):
    def inner():
        a=num()
        add=a+5
        return add
    return inner    



@decor
def num():
    return 10
forNumValues=num()    
print(num()) 
print(forNumValues)