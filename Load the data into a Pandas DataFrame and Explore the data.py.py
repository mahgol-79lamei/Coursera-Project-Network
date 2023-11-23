#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import random


# In[2]:


# Define the list of categories
categories = ['Food', 'Travel', 'Fashion', 'Fitness', 'Music', 'Culture', 'Family', 'Health']


# In[3]:


# Number of entries (n)
n = 500

# Generate random data
data = {
    'Date': pd.date_range('2021-01-01', periods=n),
    'Category': [random.choice(categories) for _ in range(n)],
    'Likes': np.random.randint(0, 10000, size=n)
}


# In[4]:


# Create a DataFrame
df = pd.DataFrame(data)

# Print the first few rows of the DataFrame
print("DataFrame Head:")
print(df.head())

# Print DataFrame Information
print("\nDataFrame Information:")
print(df.info())

# Print DataFrame Description
print("\nDataFrame Description:")
print(df.describe())


# In[5]:



# Print the count of each 'Category' element
category_counts = df['Category'].value_counts()
print("\nCount of each 'Category' element:")
print(category_counts)


# In[ ]:





# In[ ]:




