import numpy as np

# create a 1-D array containing elements ranging from zero to twenty-seven
arry1 = np.arange(27)

# convert arry1 to a 3-D array
arry2 = arry1.reshape((3, 3, 3))
                      

print(arry2)


# In[20]:


import numpy as np

# create the first 2-D array containing elements from 1 to 6
array1 = np.array([[1, 2, 3], [4, 5, 6]])

# create the second 2-D array containing elements from 7 to 12
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# horizontally stack the two arrays together
horz_stack = np.hstack((array1, array2))

print("Horizontally stacked array:")
print(horz_stack)

# vertically stack the two arrays together
vert_stack = np.vstack((array1, array2))

print("Vertically stacked array:")
print(vert_stack)


# In[62]:


import numpy as np

# create an equally spaced sequence with a gap of 5 ranging from 0 to 100
sequence = np.arange(0, 101, 5)

print(sequence)


# In[ ]:




