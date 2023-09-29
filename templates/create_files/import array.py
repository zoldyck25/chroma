from array import *

arr1=array('i',[1,2,3,45,6,7])

def linear_search(array):
       for i in array:
        print (i ) 
print(linear_search(arr1))


print (arr1[3])


arr1.append(2)
print (arr1)

arr1.insert(2,99)
print (arr1)



print(arr1[:])