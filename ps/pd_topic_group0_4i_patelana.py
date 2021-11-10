# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Topic Title](#Topic-Title) 
# + [Topic 2 Title](#Topic-2-Title)

# ## Topic Title
# Include a title slide with a short title for your content.
# Write your name in *bold* on your title slide. 

# ## Pandas Topic ##
# 
# ## pd. query ##
# **Name: Anandkumar Patel**
# ###### Email: patelana@umich.edu
# ###### Unique ID: patelana

# ### Arguments and Output
# 
# **Arguments** 
# 
# * expression (expr) 
# * inplace (default = False) 
#     * Do you want to operate directly on the dataframe or create new one
# * kwargs (keyword arguments)
# 
# **Returns** 
# * Dataframe from provided query

# ## Why
# 
# * Similar to an SQL query 
# * Can help you filter data by querying
# * Returns a subset of the DataFrame
# * loc and iloc can be used to query either rows or columns

# ## Query Syntax
# 
# * yourdataframe.query(expression, inplace = True/False

# ## Code Example

# In[2]:


import pandas as pd
df = pd.DataFrame({'A': range(1, 6),
                   'B': range(10, 0, -2),
                   'C C': range(10, 5, -1)})
print(df)

print('Below is the results of the query')

print(df.query('A > B'))
