# # Python code to merge dict using update() method
# def Merge(dict1, dict2):
# 	return(dict2.update(dict1))
	
# # Driver code
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'b': 8, 'c': 4}

# # This return None
# print(Merge(dict1, dict2))

# # changes made in dict2
# print(dict2)


def merge(a,c):
    return(a.update(c))









a={"a":2,"b":3}
c={"c":4,"g":8}
print(merge(a,c))
print(a)

