#numpy
import numpy as np
import time
import sys
# # this to check the less memory space taken by the numpy array
# l=range(1000)
# print(sys.getsizeof(5)*len(l))

# array=np.arange(1000)
# print(array.size*array.itemsize)
# #



#this demote the faster
SIZE=10000000
l1=range(SIZE)
l2=range(SIZE)

a1=np.arange(SIZE)
a2=np.arange(SIZE)

print(l1)
print(a1)

# #python list
# start=time.time()
# result=[(x+y) for x,y in zip(l1,l2)]
# print("python list took: ",(time.time()-start)*1000)
# #numpy array
# start=time.time()
# result=a1+a2
# print("numpy took the time: ",(time.time()-start)*1000)



#2d numpy array
# a=np.array([[1,2],[3,4],[5,6]])
# print(a.ndim)


# b=np.array([5,6,9])
# b.ndim              # this andim will provide the dimension of the array
# print(b.itemsize)   # this give an size of an element in bytes
# print(a.dtype)      # this is to check the data type

# c=np.array([[1,2],[3,4],[5,6]],dtype=np.float64)
# print(c)

# print(c.size)
# print(c.shape)
# print(np.zeros((3,4)))
# print(np.arange(1,5))       #this will give an array rather than the list
# print(np.linspace(1,5,10))
# print(c.reshape(2,3)) 
# print(c.ravel())
# print(c.min())
# print(c.max())
# print(c.sum())
# print(c.sum(axis=1))
# print(np.sqrt(c))
# print(np.std(c))

# v=np.array([[1,2],[3,4]])
# z=np.array([[5,6],[7,8]])
# print(v+z)
# print(v*z)
# print(v/z)
# print(v.dot(z))



#slicing "" same assimple python list
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a[0:2,2])
# print(a[-1,0:2])

#sticking 
# a=np.arange().reshape(3,2)
# b=np.arange(6,12).reshape(3,2)
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))
# a=np.arange(30).reshape(2,15)
# print(np.hsplit(a,3))
# print(np.vsplit(a,3))


# #iterate the numpy array using the nditer
# a=np.arange(12).reshape(3,4)
# print(a)
# for i in a:
#     for cell in i:
#         print(cell)
# for i in a.flatten():
#     print(i) 

# for x in np.nditer(a,order='F',flags=['external_loop']):
#     print(x)

import csv
