#!/usr/bin/env python
# coding: utf-8

# ### Heroes Of Pymoli Data Analysis
# * Of the 1163 active players, the vast majority are male (84%). There also exists, a smaller, but notable proportion of female players (14%).
# 
# * Our peak age demographic falls between 20-24 (44.8%) with secondary groups falling between 15-19 (18.60%) and 25-29 (13.4%).  
# -----

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[16]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)

purchase_data


# ## Player Count

# * Display the total number of players
# 

# In[17]:


total_players = pd.DataFrame({"Total Players":[purchase_data["SN"].nunique()]})

total_players


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[18]:


purchase_breakdown = pd.DataFrame({"Number of Unique Items":[purchase_data["Item Name"].nunique()],
                                  "Average Price":[purchase_data["Price"].mean()],
                                   "Total Purchases":[purchase_data["Price"].count()],
                                   "Amount Purchased":[purchase_data["Price"].sum()]})

pd.options.display.float_format = '${:,.2f}'.format

purchase_breakdown


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[29]:


#Grouping by gender
players_df= purchase_data.groupby(['Gender'])
#finding total players
#total players from gender grouped dataframe
players_gender = players_df["SN"].nunique()
#Finding Percentages
players_percent = total_players_gender / purchase_data["SN"].nunique() * 100

#merge dataframes 
total_gender_count = pd.concat([players_gender.rename("Total Player Count"),players_percent.rename("Total Percent")],axis=1)

#sort, format percent column, output result
total_gender_count.sort_values(["Total Player Count"], ascending = False).style.format({"Total Percent":'{:.2f}%'})


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[43]:


#collect purchase data variables
Purchase_count= players_df["Item ID"].count()
avg_purchase_price = players_df["Price"].mean()
Total_purchase_price = players_df["Price"].sum()

avg_purchase_Gender = Total_purchase_price / Purchase_count

#merge dataframes into full analysis, give series column names here
purchase_analysis_gender = pd.concat([Purchase_count.rename("Purchase Count"),avg_purchase_price.rename("Average Purchase Price"),Total_purchase_price.rename("Total Purchase Value"),avg_purchase_Gender.rename("Avg Total Purchase per Person")],axis=1)

#format for nice display
#format for price, output result
purchase_analysis_gender.style.format({'Average Purchase Price':"\${:,.2f}", 'Total Purchase Value': "\${:,.2f}", 'Avg Total Purchase per Person': "\${:,.2f}"})


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[44]:



#define bins 
bins = [0, 9, 14, 19, 24, 29, 34, 39, 200]
labels = ['<10', '10-14', '15-19', '20-24', '26-29', '30-34', '35-39', '40+']

#add binned data to new  Group column in original df 
purchase_data["Age Group"] = pd.cut(purchase_data['Age'], bins, labels = labels)

#new dataframe grouped by bins
purchase_data_age_group =  purchase_data.groupby("Age Group")

#find how many players in each bin
total_player_count_age=purchase_data_age_group["SN"].nunique()

#find what percent of tatal players each bin represents
total_player_percent_age = total_player_count_age / purchase_data["SN"].nunique() * 100

#merge dataframes into full analysis, give series column names here
total_players_count_age = pd.concat([total_player_count_age.rename('Total Count'),total_player_percent_age.rename('Percentage of Players')],axis=1)

#format for nice display
#format for price, output result
total_players_count_age.style.format({"Percentage of Players":"{:.2f}%"})


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[45]:


#collect purchase data variables
Purchase_count_age= purchase_data_age_group["Item ID"].count()
avg_purchase_price_age = purchase_data_age_group["Price"].mean()
Total_purchase_price_age = purchase_data_age_group["Price"].sum()

avg_purchase_age = Total_purchase_price_age / Purchase_count_age

#merge dataframes into full analysis, give series column names here
purchase_analysis_age = pd.concat([Purchase_count_age.rename("Purchase Count"),
                                   avg_purchase_price_age.rename("Average Purchase Price"),
                                   Total_purchase_price_age.rename("Total Purchase Value"),
                                   avg_purchase_age.rename("Avg Total Purchase per Person")],axis=1)

#format for price, output result
purchase_analysis_age.style.format({'Average Purchase Price':"\${:,.2f}", 'Total Purchase Value': "\${:,.2f}", 'Avg Total Purchase per Person': "\${:,.2f}"})


# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[59]:


purchase_data_name =  purchase_data.groupby("SN")
#collect purchase data variables
Purchase_count_name= purchase_data_name["Item ID"].count()
avg_purchase_price_name = purchase_data_name["Price"].mean()
Total_purchase_price_name = purchase_data_name["Price"].sum()


#merge dataframes
purchase_analysis_name = pd.concat([Purchase_count_name.rename("Purchase Count"),
                                   avg_purchase_price_name.rename("Average Purchase Price"),
                                   Total_purchase_price_name.rename("Total Purchase Value")],axis=1)

#format for price, output result

purchase_analysis_name.sort_values(["Purchase Count"], ascending = False).head(10).style.format({'Item Price':"\${:,.2f}", 'Total Purchase Value': "\${:,.2f}"})


# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[57]:


#make new dataframe 
most_popular_df = purchase_data[['Item ID','Item Name', 'Price']]

#group new frame 
most_popular_df = most_popular_df.groupby(["Item ID","Item Name"])

#total purchases from item grouped dataframe
total_purchase_count_item = most_popular_df["Item ID"].count()

#total purchase value from item grouped dataframe
total_purchase_value_item = (most_popular_df["Price"].sum())
 
#item price, can't figure out how to directly pull so will do math instead
item_price_item = total_purchase_value_item / total_purchase_count_item


most_popular_analysis = pd.concat([total_purchase_count_item.rename('Purchase Count'), item_price_item.rename('Item Price'), total_purchase_value_item.rename('Total Purchase Value')],axis=1)

#format for price
most_popular_analysis.sort_values(["Purchase Count"], ascending = False).head().style.format({'Item Price':"\${:,.2f}", 'Total Purchase Value': "\${:,.2f}"})


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[60]:


most_popular_analysis.sort_values(["Total Purchase Value"], ascending = False).head().style.format({'Item Price': "\${:,.2f}", 'Total Purchase Value': "\${:,.2f}"})

