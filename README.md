
Instagram Profile & Posts 
================================================
![insta](https://github.com/user-attachments/assets/a87b6d9c-4f3d-422f-9c52-ff7e560ce465)


Sapienza University of Rome

Algorithmic Methods of Data Mining (Sc.M. in Data Science)

Goal: 
================================================
Nowadays, social media is widely used, taking significant importance in people's lives and influencing how they live. Moreover, social media, which is here to stay, has substantially impacted how people communicate. Thus, available on iPhone and Android, Instagram is a free picture and video-sharing app. Their service allows users to post photographs and videos that they may then share with their followers or a small group of friends. In addition, they can also browse, comment on, and "like" the Instagram posts their friends have shared.

Imagine that you all have been hired as Data Scientists at Instagram. You and your team have to analyse the posts received by users worldwide. Each row in the datasets may represent a post, a profile or a location associated with the posts done.

Your goal is to answer some research questions (RQs) that may help them discover and interpret meaningful patterns in data and eventually understand how a user behaves on this social network.


## Datasets:

------------------------------------------------
Go to this website and download the whole dataset, make sure it includes the files instagram_profiles.csv, instagram_posts.csv and instagram_locations.csv.

### Research questions

--------------------------------------------------

[RQ1] After collecting information, the Data Scientists have to know what dataset they are dealing with, so let's start with an Exploratory Data Analysis (EDA). What can you say about our datasets? Please summarise its main characteristics with visual and tabular methods.

[RQ2] Let's explore the dataset by finding simple insights regarding the profile and posts.

Plot the number of posts for each profile in descending order.
What posts have the highest number of "likes"?
What posts have the most and the least number of comments?
How many posts include tagged locations, and how many do not? Show it using an appropriate chart and comment your results.
How many posts include only photos? How many also have videos?
What's the percentage of business accounts vs non-business? What can you interpret regarding that percentage?
[RQ3] Now it's important to understand the most common times in which users publish their posts

What is the most common time in which users publish their posts?
Create a function that receives a time intervals list as a parameter and returns a plot with the number of posts for each given interval.

[RQ4] In most cases, we will not have a consistent dataset, and the one we are dealing with is not an exception (ex. in the given datasets, you may not find the information of the profiles for some of the posts). So let’s enhance our analysis.

Write a function that, given a profile_id, will be able to return the posts that belong to the given profile_id.
Write another function that, given an input n (an integer), will return the posts that belong to the n top posted profiles (top n profiles that have posted the highest number of posts) that their data is available in the profile.csv using the previously written function.
What is the average number of "likes" and comments of the top 10 profiles with the highest number of posts which their information is available in profile.csv?
Plot the number of posts that these top 10 profiles have sent on Instagram in the given interval in question RQ3. Interpret the resulting chart.
[RQ5] The most influential users are the ones with the highest number of “followers", you can now look more into their activity.

Plot the top 10 most popular users in terms of followers and their number of posts.
Who is the most influential user?
Have they posted anything with tagged locations? Extract the most frequent areas on their posts and plot the number of times each city has been visited.
How many pictures-only posts have they published? How many reels? (only videos) and how many with both contents? Provide the number as percentages and interpret those figures.
How many "likes" and comments did posts with only pictures receive? How about videos and mixed posts? Try to provide the average numbers and confront them with their followers amount, explaining what you can say from that comparison.
[RQ6] It's time to get information from the user posting effectiveness.

What is the average time (days and minutes) a user lets pass before publishing another post? Plot the top 3 users that publish posts more frequently (calculate the average time that passes between posts), including their amount of followers and following. Provide insights from that chart.
Using the function you previously coded, plot the time intervals with the highest average number of “likes” and the ones with the highest average number of comments on posts.
[RQ7] Of course, calculating probabilities is a job that any Data Scientist must know. So let's compute some engaging figures.

What's the probability that a post receives more than 20% "likes" of the number of followers a user has?
Do users usually return to locations? Extract the probability that a user returns to a site after having posted it in the past. Does that probability make sense to you? Explain why or why not.
[RQ8] Every decision you take in a data-based environment should be reinforced with charts, statistical tests and analysis methods to check whether a hypothesis is correct or not.

Does more “likes” also mean more comments? Plot a scatter plot of “likes” vs comments for posts.
Can you find any significant relationship between the time a user publishes a post and the number of comments and “likes”? Use an appropriate statistical test or technique and support your choice.
What’s the distribution of followers? Plot the empirical distribution of followers amongst all users and extract the mean, mode, and quantiles. Interpret those figures.
What are histograms, bar plots, scatterplots and pie charts used for?
What insights can you extract from a Box Plot?
Bonus points
Up to this point, you probably have worked with one or two files simultaneously. Nevertheless, for the literals a. and b. of this section, you must work with the three datasets at the same time. Note that performing some of these operations might be too complex for your pc specs. For this reason, we suggest you make use of AWS (yeah! only a suggestion). In case you need it, in the following links you can find the same three files already mounted into AWS for you to work with them easily (instagram_posts, instagram_profiles, instagram_locations).

a. Sort the users in terms of number of followers and divide them into two groups: for the first group, take only the top 10% regarding "followers", and for the second one, take the rest. Now compare the mean of time intervals between posts for the two categories. Do you notice something relevant?

b. Assume users publish their posts the same day pictures or videos are taken: Are there users that have visited the same location on the same day? How about the same week? Extract the results and explain them.

c. Implement a text data analysis (also known as text mining) of the field "description" from instagram_posts.csv for descriptions written in English. Use appropriate visualizations and statistics to highlight the words (and probably the topics) provided for the users in that field.

-----------------------------------------------------

## Script descriptions:

---------------------------------------------------

1. `README.md`:
   
   > A markdown file which you are reading right now explaining how we worked and the descriptions of our Github repository.

2. `RQ1_RQ2_RQ7_RQ8_AQ1.ipynb`:
   
   >This script provides our analysis of the different datasets, for the questions: RQ1, RQ2, RQ7, RQ8 and the AQ1.  
   >Done by Flavio Brizzolari scrocco

3. `RQ3_RQ4_AQ2.ipynb`:
   
   >This script provides our analysis of the different datasets for the questions: RQ3, RQ4 and the AQ2.  
   >Done by Viktoriia Vlasenko.
   
4. `RQ5_RQ6.ipynb`:
   
   >This script provides our analysis of the different datasets for the questions: RQ5, RQ5.  
   >Done by Vahid ghanbarizadeh.

3. `adm2.py`:
   
   > A python file with functions needed for `RQ3_RQ4_AQ2.ipynb`.
    
4. `commandline.sh`:
    
    >A .sh file to answer the command line questions of our assignment, a terminal based analysis.
    >Done by Vahid ghanbarizadeh.

2. `functions.py`:
   
   >A python file containing the functions needed for `RQ1_RQ2_RQ7_RQ8_AQ1.ipynb`.

**. `ADM.HW2.Group24 files.ipynb `:

   >A This script provides our analysis of the different datasets for the all questions
