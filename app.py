#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd # for dataframes
import numpy as np # for NaN
import matplotlib.pyplot as plt # for visualization
import seaborn as sns
import streamlit as st


# In[27]:


'''
# Creating Web Apps with JN and Streamlit
## Christian F. Jung
christianfjung.com

**About this Project** 

This project uses live poll data from 538 so the website will be update constantly!

'''


# In[4]:


df_online= pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/media-mentions-2020/online_weekly.csv")
df_online.head()


# # Most Online Attention to this Date
# 

# In[6]:


dfO= df_online[['name','matched_stories']]

dfO= dfO.groupby("name")["matched_stories"].sum()
dfO = pd.DataFrame(dfO)

dfToShow= dfO.sort_values("matched_stories", ascending=False)
dfToShow.head()


# In[23]:


st.bar_chart(dfToShow)


# In[ ]:




# # What does the script do? 
# 

# Converts NB to .py
# `jupyter nbconvert   --to script YOURNAME.ipynb`
# 
# 
# 
# 
# 
# Runs the local streamlit app
# `streamlit run app.py`

# In[ ]:




# ## Try it on your own with cable data:
# `df_cable= pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/media-mentions-2020/cable_weekly.csv")` 
# 

# In[ ]:




