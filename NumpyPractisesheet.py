#!/usr/bin/env python
# coding: utf-8

# # NumPy Exercises - Solutions
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks and then you'll be asked some more complicated questions.
# 
# Import NumPy as np

# In[1]:


import numpy as np


# # create an array of 10 zeroes

# In[5]:


np.zeros(10)


# # create an array of 10 ones

# In[6]:


np.ones(10)


# # Create an array of 10 fives

# In[7]:


np.ones(10)*5


# # Create an array of the integers from 10 to 50

# In[11]:


np.arange(10,51,2)


# # Create an array of all the even integers from 10 to 50

# In[16]:


np.arange(10,51,2)


# Create a 3x3 matrix with values ranging from 0 to 8

# In[17]:



np.arange(0, 9).reshape(3,3)


# # Create a 3x3 identity matrix

# In[18]:


np.identity(3)


# # Use NumPy to generate a random number between 0 and 1

# In[19]:


np.random.normal(0,1,1)


# # Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
# 

# In[21]:


np.random.normal(0,1,25)


# # Create the following matrix:

# In[22]:


np.array([[ 0.01,  0.02,  0.03,  0.04,  0.05,  0.06,  0.07,  0.08,  0.09,  0.1 ],
       [ 0.11,  0.12,  0.13,  0.14,  0.15,  0.16,  0.17,  0.18,  0.19,  0.2 ],
       [ 0.21,  0.22,  0.23,  0.24,  0.25,  0.26,  0.27,  0.28,  0.29,  0.3 ],
       [ 0.31,  0.32,  0.33,  0.34,  0.35,  0.36,  0.37,  0.38,  0.39,  0.4 ],
       [ 0.41,  0.42,  0.43,  0.44,  0.45,  0.46,  0.47,  0.48,  0.49,  0.5 ],
       [ 0.51,  0.52,  0.53,  0.54,  0.55,  0.56,  0.57,  0.58,  0.59,  0.6 ],
       [ 0.61,  0.62,  0.63,  0.64,  0.65,  0.66,  0.67,  0.68,  0.69,  0.7 ],
       [ 0.71,  0.72,  0.73,  0.74,  0.75,  0.76,  0.77,  0.78,  0.79,  0.8 ],
       [ 0.81,  0.82,  0.83,  0.84,  0.85,  0.86,  0.87,  0.88,  0.89,  0.9 ],
       [ 0.91,  0.92,  0.93,  0.94,  0.95,  0.96,  0.97,  0.98,  0.99,  1.  ]])


# # Create an array of 20 linearly spaced points between 0 and 1:

# In[24]:


np.linspace(0,1,20)


# # Numpy Indexing and Selection
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[25]:


arr=np.arange(1,26).reshape(5,5)


# In[27]:


np.arange(1,26).reshape(5,5)

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# In[28]:


arr[2:,1:]

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# In[30]:


arr[3,4]

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# In[31]:


arr[:3,1:2]

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# In[32]:


arr[4:,0:]

# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
# In[33]:


arr[3:,0:]


# # Now do the following
# Get the sum of all the values in mat

# In[34]:


arr.sum()


# # Get the standard deviation of the values in mat

# In[36]:


np.std(arr)


# # Get the sum of all the columns in mat

# In[38]:


arr.sum( axis=0)


# In[ ]:


