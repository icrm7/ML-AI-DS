#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning & Visualization

# klib is a Python library for importing, cleaning, analyzing and preprocessing data.
# 
# ## klib.describe - Functions for visualizing datasets
# - klib.cat_plot(df) # returns a visualization of the number and frequency of categorical features
# - klib.corr_mat(df) # returns a color-encoded correlation matrix
# - klib.corr_plot(df) # returns a color-encoded heatmap, ideal for correlations
# - klib.dist_plot(df) # returns a distribution plot for every numeric feature
# - klib.missingval_plot(df) # returns a figure containing information about missing values
# 
# ## klib.clean - Functions for cleaning datasets
# - klib.data_cleaning(df) # performs datacleaning (drop duplicates & empty rows/cols, adjust dtypes,...)
# - klib.clean_column_names(df) # cleans and standardizes column names, also called inside data_cleaning()
# - klib.convert_datatypes(df) # converts existing to more efficient dtypes, also called inside data_cleaning()
# - klib.drop_missing(df) # drops missing values, also called in data_cleaning()
# - klib.mv_col_handling(df) # drops features with high ratio of missing vals based on informational content
# - klib.pool_duplicate_subsets(df) # pools subset of cols based on duplicates with min. loss of information
# 
# ## klib.preprocess - Functions for data preprocessing (feature selection, scaling)
# - klib.train_dev_test_split(df) # splits a dataset and a label into train, optionally dev and test sets
# - klib.feature_selection_pipe() # provides common operations for feature selection
# - klib.num_pipe() # provides common operations for preprocessing of numerical data
# - klib.cat_pipe() # provides common operations for preprocessing of categorical data
# - klib.preprocess.ColumnSelector() # selects num or cat columns, ideal for a Feature Union or Pipeline
# - klib.preprocess.PipeInfo() # prints out the shape of the data at the specified step of a Pipeline
# 

# In[5]:


#pip install -U klib
#conda install -c conda-forge klib


# In[3]:


import klib
import pandas as pd


# In[7]:


data = pd.read_csv(r"C:\Users\Lenovo\Desktop\Data Sets\Cancer_Data.csv") #Reading the data from csv file
data.head() #First five records


# In[8]:


data.info() 


# In[9]:


data_clean = klib.data_cleaning(data)
#klib.data_cleaning() does the job of klib.clean_column_names(), klib.convert_datatypes(), klib.drop_missing(  ) 


# In[10]:


data_clean.info()


# In[ ]:




