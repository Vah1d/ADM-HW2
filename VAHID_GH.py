#!/usr/bin/env python
# coding: utf-8

# In[84]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns 
import tqdm as tq
from matplotlib import style
import warnings


# #### [RQ1] Exploratory Data Analysis
# 

# One step is to observe the head of the data to have a first visual approach of the table under examination. Proceed by displaying only the first 5 observations. After the first phase of exploration of data types, characteristics are extracted from the data.

# In[3]:


df_prof = pd.read_csv ('instagram_profiles.csv', delimiter='\t' )
df_prof.head()


# In[3]:


df_post = pd.read_csv("instagram_posts.csv", delimiter='\t', nrows=10000)
df_post.head()


# In[36]:


df_post.info()


# In[4]:


df_loc = pd.read_csv ('instagram_locations.csv', delimiter='\t' )
df_loc.head()


# RQ5 The most influential users are the ones with the highest number of “followers", you can now look more into their activity.

#  1. Plot the top 10 most popular users in terms of followers and their number of posts.

# In[11]:


#load just the columns which we need 
Top10 = pd.DataFrame(df_prof.loc[:,["profile_id", "followers","n_posts",]])
#avoid the "Nan" problem
Top10.fillna(0,inplace = True)     
#sort by top 10 
Top10 = Top10.sort_values(by=["followers"],ascending=False).head(10)   
#plot it 
Top10.plot(kind = "bar",x = "profile_id", y = "n_posts")
Top10


# 2. Who is the most influential user?

# In[12]:


Top10.head(1)


# 3. Have they posted anything with tagged locations? Extract the most frequent areas on their posts and plot the number of times each city has been visited

# In[13]:


#extract top 10 user and build the dataframe:

t10 = Top10[["profile_id"]]
t10


# In[14]:


#merging top 10 profiles and their locations from df_posts
top10_loc = pd.DataFrame(columns = ["profile_id","post_id","location_id",])
for chunk in pd.read_csv('instagram_posts.csv',on_bad_lines = "skip",sep = "\t",chunksize= 500000,usecols=["profile_id","post_id","location_id"]):
    top10loc= pd.merge(chunk,t10)
    top10_loc = pd.concat([top10_loc ,top10loc])
    
top10_loc


# In[16]:


#building a new dataframe with posts and location's name of the top 10 profile ids 
loctag = pd.merge(top10_loc,df_loc[["id","name"]],left_on = "location_id",right_on="id")
loctag


# In[17]:


#the most frequent areas:
most = loctag.groupby("name").count()
most.sort_values(by="profile_id",ascending=False).head(10)


# In[18]:


#the most frequent areas plot
most_frequent = most.sort_values(by="profile_id",ascending=False).head(10)
most_frequent.plot(kind="bar",y = "location_id")
plt.xlabel("location's name", labelpad = 14)
plt.ylabel("numebrs of visiting", labelpad = 14)
plt.title("Most frequent areas have been visited ", y = 1.05)


# 5-4 How many pictures-only posts have they published? How many reels? (only videos) and how many with both contents? Provide the number as percentages and interpret those figures.

# In[33]:


#extracting post_type column from instagram_post and building a new dataframe
pic_reel = pd.DataFrame(columns = ["profile_id","post_id","post_type"])
for chunk in pd.read_csv('instagram_posts.csv',on_bad_lines = "skip",sep = "\t",chunksize= 500000,usecols=["profile_id","post_id","post_type"]):
    post_type= pd.merge(chunk,t10)
    pic_reel = pd.concat([pic_reel,post_type])
    
pic_reel


# In[20]:


#sorting
pic_reels = pic_reel.groupby("post_type").count()
pic_reels


# In[21]:


pic_reels["percentage"] = (pic_reels['profile_id'] / pic_reels['profile_id'].sum()) * 100
pic_reels["percentage"].plot(kind="bar")
plt.xlabel(" pictures-only                                     reels-only", labelpad = 14)
plt.title("percentages of picture and reels have published ", y = 1.05)


# As we can see from the plot top 10 users have published picture-only posts approximatly 4 times more then reels_only posts. and also they published 128 pictures_only and 13 reels_only. It is important to be mention that they hidden some of their posts and reels after get more users and this numbers are not the real activity of them from the starting of their pages.

# 5.5 How many "likes" and comments did posts with only pictures receive? How about videos and mixed posts? Try to provide the average numbers and confront them with their followers amount, explaining what you can say from that comparison.

# In[37]:


#building a dataframe consist of  likes and comments on the posts of the top 10 users.
like_comment = pd.DataFrame(columns = ["profile_id","post_id","post_type","numbr_likes","number_comments"])
for chunk in pd.read_csv('instagram_posts.csv',on_bad_lines = "skip",sep = "\t",chunksize= 500000,usecols=["profile_id","post_id","post_type","numbr_likes","number_comments"]):
    comment= pd.merge(chunk,t10)
    like_comment = pd.concat([like_comment,comment])
    
like_comment


# In[23]:


#extract number of followers from profile and merging with our new dataframe:
num_like = like_comment[["profile_id","post_type","numbr_likes","number_comments"]]
fol = pd.DataFrame(df_prof[["followers","profile_id"]])
summation= pd.merge(num_like,fol,on="profile_id")
# sum the number of likes and comment base on the 2 types (reel and picture)
summation[["post_type","numbr_likes","number_comments"]].groupby("post_type").sum()


# In[53]:


#total number of like and comments of each user
total = summation[["profile_id","numbr_likes","number_comments"]].groupby("profile_id").agg(np.average)
total


# In[54]:


#averaging of the likes and comments for top 10 users 
average = summation[["profile_id","numbr_likes","number_comments"]].groupby("profile_id").agg(np.average)
average = average.rename(columns={"numbr_likes": "average of like", "number_comments": "average of comments"})
average = average.round({'average of like': 1, 'average of comments': 1})
average


# In[46]:


#Adding number of followers from TOP10
final = pd.merge(average,Top10,on = "profile_id")
final


# In[57]:


# merging to have all data in one table 
fin = pd.merge(final,total,on = "profile_id")
fin


# In[60]:


#calculating the average of comment and lik for each users
fin ['engagment_rate'] = ((fin ['numbr_likes'] + fin['number_comments']) / fin['followers'])*100
engagment_rate = fin.sort_values(by="followers",ascending=False)
engagment_rate 


# One of the most important consept in social media is ENGAGMENT RATE.
# Engagement rate measures the amount of interaction social media content earns relative to reach or followers or audience size.
# To calculate the Instagram engagement rate for a post, divide the total number of likes and comments by your follower count, and then multiply by 100 to give you a percentage.
# So as we could see from the last table although the fist one with more that 285 millions followers, it has .31% engagment rate. 
# Among top 10 influencers of our database, the last one with around 26 millions of user has the most engagment rate.

# RQ 6. It's time to get information from the user posting effectiveness.

# 6.1 What is the average time (days and minutes) a user lets pass before publishing another post? Plot the top 3 users that publish posts more frequently (calculate the average time that passes between posts), including their amount of followers and following. Provide insights from that chart.

# 6.1.1 Average time (days and minutes) a user lets pass before publishing another post?

# In[44]:


# importing the columns needed for this question from posts csv file
ave_time = pd.DataFrame(columns = ["profile_id", "cts","number_comments","numbr_likes"])
for chunk in pd.read_csv('instagram_posts.csv', on_bad_lines = "skip", sep="\t",chunksize=500000,usecols=["profile_id", "cts","number_comments","numbr_likes"]):
    
    ave_time =pd.concat([chunk, ave_time])
ave_time


# In[45]:


#changing the format of timestamp
ave_time['cts'] = pd.to_datetime(ave_time['cts'], format='%Y-%m-%d %H:%M:%S.%f')


# In[54]:


# calculating the first and last posts each user published
top20 = ave_time.groupby("profile_id").aggregate({'cts':["max", "min", "count"]})


# In[59]:


# counting users published more than 1 post 
top20 =  top20 [top20.cts["count"] > 1]
# calculating the average of time for publishing between posts for each users
top20 ["meantime_of_publishing_posts"] = (top20 .cts['max'] - top20 .cts['min']) / (top20 .cts['count']-1)
top20


# In[48]:


#extracting followers and followinng from 
follower_ing = df_prof[["profile_id","followers", "following"]]
follower_ing


# In[61]:


# merging for adding followers and following 
fol = pd.merge(top20,follower_ing ,on = "profile_id",)
fol


# In[50]:


# average time between two posts
meantime = top20["meantime_of_publishing_posts"].mean()
print("average time between two posts for all users:", str(meantime))


# 6.1.1Plot the top 3 users that publish posts more frequently (calculate the average time that passes between posts), including their amount of followers and following. Provide insights from that chart.

# In[74]:


warnings.filterwarnings("ignore")
averages = top20.iloc[: , [2,3]]
mean_times_fols = pd.merge(averages, df_prof, on='profile_id')
mean_times_fols.rename(columns=''.join, inplace=True)
mean_times_fols = mean_times_fols.dropna()
mean_times_fols.sort_values(by = 'meantime_of_publishing_posts' , ascending = True)
mean_time_final = mean_times_fols[["profile_id","ctscount","meantime_of_publishing_posts","following","followers"]]
mean_time_final


# In[75]:


#Top10 = Top10.sort_values(by=["followers"],ascending=False).head(10)
top3 = mean_time_final.sort_values(by = "meantime_of_publishing_posts", ascending=True)
top3= top3.head(3)
top3


# In[85]:


style.use('seaborn-dark-palette')
ax =top3.plot(kind='bar', y=["following", "followers"], figsize=(10,8))
labels = top3.profile_id.iloc[:3]
ax.set_xticks([0,1,2], labels)
plt.title("Top 3 users'")
plt.xlabel("profile_id")
plt.show()


# 6.2 Using the function you previously coded, plot the time intervals with the highest average number of “likes” and the ones with the highest average number of comments on posts.

# In[87]:


#defining a new function for this question 
posts = ave_time


# In[89]:


# Changing the timestamps format
posts['cts'] = pd.to_datetime(posts['cts'], format='%Y-%m-%d %H:%M:%S.%f')
dfCopy = posts.copy()
# Changing the timestamps into hour
dfCopy['cts'] = dfCopy.cts.dt.hour


# In[98]:



highest = dfCopy.groupby(pd.cut(dfCopy['cts'],  np.arange(0, 26, 2)))['numbr_likes', 'number_comments'].mean()
highest.head()


# In[99]:


#calculating the highest average of like and comments 
print(f"Highest average of likes: {highest.numbr_likes.max():{2}.{5}}")
print(f"Highest average of comments: {highest.number_comments.max():{2}.{3}}")


# In[100]:


#dividing a day to 12 slots 
labels = ["00:00:00-02:00:00","02:00:00-04:00:00","04:00:00-06:00:00","06:00:00-08:00:00","08:00:00-10:00:00","10:00:00-12:00:00",
         "12:00:00-14:00:00", "14:00:00-16:00:00","16:00:00-18:00:00","18:00:00-20:00:00","20:00:00-22:00:00","22:00:00-23:59:59"]
#plot the average number of likes recorded every 2 hours 
style.use('seaborn-dark-palette')
highest.plot(kind='bar', y='numbr_likes', figsize=(8,6))
plt.title("Average number of likes recorded every 2 hours")
plt.xlabel("\ntime slots of a day")
plt.ylabel("Average number of likes.")
plt.xticks(ticks=np.arange(0,12,1),labels=labels)
plt.show()


# In[103]:


#polting the average of comments recorded every 2 hours 
highest.plot(kind='bar', y='number_comments', figsize=(8,6))
plt.title("Average number of comments recorded every 2 hours")
plt.xlabel("\ntime slots of a day.")
plt.ylabel("Average number of likes.")
plt.xticks(ticks=np.arange(0,12,1),labels=labels)
plt.show()


# As we could see from above from 18 to 20 users got the most comments , while during 16 to 18 they got more likes 
