'''
import numpy as np
#1-D array
x=np.array([12,43,65])
print(x)



import numpy as np
#2-D array
#4x3 matrix
x=np.array([[12,43,65],
           [32,11,77],
           [12,90,65],
           [3,6,99]])
print(x)




import numpy as np
#2-D array
#3x4 matrix
x=np.array([[12,43,65,31],
           [32,11,77,87],
           [12,90,65,12]])
print(x)
#shape
print(x.shape)





import numpy as np
#2-D array
#4x3 matrix
x=np.array([[12,43,65],
           [32,11,77],
           [12,90,65],
           [6,78,91]])
print(x)
y=x.reshape(6,2)
print(y)





import numpy as np
#1-D----0 to 9
x=np.arange(10)
print(x)




import numpy as np
#1-D----3 to 29
x=np.arange(3,30)
print(x)





import numpy as np
#1-D----5 to 50 step of 5
x=np.arange(5,51,5)
print(x)




#print table of 5...each row 2 value
import numpy as np
x=np.arange(5,51,5)
y=x.reshape(5,2)
print(y)





import numpy as np
#1D all zero values
x=np.zeros(5)
print(x)




import numpy as np
#2D all zero values
x=np.zeros((3,3))
print(x)





import numpy as np
#1D all one values
x=np.ones(7)
print(x)




import numpy as np
#2D all one values
x=np.ones((3,4))
print(x)





import numpy as np
x=np.linspace(10,50,7)
print(x)





import numpy as np
x=np.array([32,1,5,4,3,1,6,9])
#start 2 gap of 2 till 6 index
y=slice(2,7,2)
print(x[y])





import numpy as np
x=np.array([32,1,5,4,3,1,6,9])
#start 2 gap of 2 till 6 index
y=x[2:7:2]
print(y)





import numpy as np
#slice on 2d array
x=np.array([[32,54,6],
            [12,54,2],
            [11,54,21],
            [9,8,11]])
#any row 2 column
print(x[...,2])
#2nd row any value
print(x[2,...])
#any row column 1 onwards
print(x[...,1:])





import numpy as np
#2d array
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21],
            [9,8,11]])
#conditional data
print(x[x>25])





import numpy as np
#2d array broadcast
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21]])
y=np.array([[2,4,6],
            [1,13,27],
            [90,45,19]])
print(x+y)
print(x-y)
print(x*y)
print(x/y)






import numpy as np
#2d array broadcast
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21]])
y=np.array([[2,4,6],
            [1,13,27],
            [90,45,19]])
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))




import numpy as np
#2d array broadcast
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21]])
y=np.array([[2,4,6],
            [1,13,2],
            [9,5,9]])
print(np.mod(x,y))




import numpy as np
#transpose
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21]])
print(np.transpose(x))



import numpy as np
#transpose
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21]])
print(x.T)





import numpy as np
#flatten
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21]])
print(x.flatten())



import numpy as np
#flatten
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21]])
print(x.flatten())
#f style ordering
print(x.flatten(order='F'))





import numpy as np
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21]])
y=np.array([[2,4,5],
            [4,3,1],
            [8,7,4]])
print(np.concatenate((x,y)))



import numpy as np
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21]])
y=np.array([[2,4,5],
            [4,3,1],
            [8,7,4]])
print(np.concatenate((x,y),axis=1))





import numpy as np
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21],
            [3,6,8]])
print(np.split(x,2))



import numpy as np
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21],
            [3,6,8]])
#unique
print(np.unique(x))



import numpy as np
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21],
            [3,6,8]])
#min
print(np.amin(x))
#min col wise
print(np.amin(x,0))
#min row wise
print(np.amin(x,1))
#max
print(np.amax(x))
#max col wise
print(np.amax(x,0))
#max row wise
print(np.amax(x,1))






import numpy as np
x=np.array([[32,54,6],
            [12,51,2],
            [11,54,21],
            [3,6,8]])
#mean
print(np.mean(x))
#median
print(np.median(x))





import numpy as np
x=np.array([[0,54,6],
            [12,0,2],
            [0,54,21],
            [3,0,0]])
print(np.nonzero(x))






import numpy as np
#string handling
x='this is PYTHON'
print(np.char.lower(x))
print(np.char.upper(x))
print(np.char.title(x))
print(np.char.capitalize(x))
r=np.char.replace(x,'this','that')
print(r)
print(np.char.multiply('Hello',5))
print(np.char.add('Hello','Python'))

'''











