import pandas as pd
from datetime import time
import matplotlib.pyplot as plt

def dataset_dtypes(dataset):
    """
    dataset types - .dtypes
    """
    df = pd.read_csv(
        dataset, 
        delimiter='\t', 
        encoding = 'ISO-8859-1')
    print(df.dtypes)


def dataset_info(dataset):
    """
    FINISH
    dataset information - .info()
    """
    df = pd.read_csv(
        dataset, 
        delimiter='\t', 
        chunksize=5,
        encoding = 'ISO-8859-1')
    print(df.info())
    
def import_dataset_columns(dataset, columns, chunksize):
    df = pd.read_csv(
        dataset, 
        delimiter='\t', 
        chunksize=chunksize, 
        encoding = 'ISO-8859-1', 
        usecols=[*columns])
    return df

def import_dataset(dataset, chunksize):
    df = pd.read_csv(
        dataset, 
        delimiter='\t', 
        chunksize=chunksize, 
        encoding = 'ISO-8859-1')
    return df

def hello(name):
    print(f"Hello, {name}!")
    

"""
1) What is the most common time in which users publish their posts?
"""
# count number of rows in interval
def time_count_in_interval(chunk, interval):
    return chunk.loc[(chunk > time.fromisoformat(interval[0])) & (chunk <= time.fromisoformat(interval[1]))].count()

# q3.1 function
def common_time(chunksize = 5):
    intervals = []
    for i in range(0, 24):
        if i < 10:
            intervals.append([f'0{i}:00:00', f'0{i}:59:59'])
        else:
            intervals.append([f'{i}:00:00', f'{i}:59:59'])
    for start, end in intervals:
        #print(start, end)
        pass
    td = {}
    df = import_dataset_columns("instagram_posts.csv", ['cts'], chunksize)
    for chunk in df:
        chunk = pd.to_datetime(chunk["cts"])
        chunk = pd.Series([val.time() for val in chunk])
        #print(chunk)
        for start, end in intervals:
            td[start+' - '+end] = time_count_in_interval(chunk, [start, end])
        break
    #print(intervals)
    max_count_of_posts = max(td.values())
    for k, v in td.items():
        if v == max_count_of_posts:
            print(f"{k}: {v} posts")

def plot_intervals_posts(intervals, chunksize = 5):
    intervals_posts = {}
    data = import_dataset_columns("instagram_posts.csv", ['cts'], chunksize)
    for chunk in data:
        chunk = pd.to_datetime(chunk["cts"])
        chunk = pd.Series([val.time() for val in chunk])
        for interval in intervals:
            anot = interval[0]+' - '+interval[1]
            intervals_posts[anot] = time_count_in_interval(chunk, interval)
        break
    print("Number of posts in time interval:")
    i = 0
    for interval, posts in intervals_posts.items():
        i += 1
        print(f"{i} interval: {interval} => {posts} posts")
    df = pd.DataFrame([intervals_posts])
    
    
    
    plt.bar(
        [f'{i+1}' for i in range(len(intervals_posts.keys()))], 
        list(intervals_posts.values())
    )

    # Labelling 

    plt.xlabel("Intervals")
    plt.ylabel("Number of posts")
    plt.title("Number of posts to time intervals")

    
# Write a function that, given a profile_id, will be able to return the posts that belong to the given profile_id
def findPostsByProfileId(profile_id, chunksize = 5):
    data = import_dataset_columns("instagram_posts.csv", 
                                  [
                                      'profile_id', 
                                      'post_id', 
                                      'post_type', 
                                      'description', 
                                      'numbr_likes',
                                      'number_comments'
                                  ], 
                                  chunksize)
    for chunk in data:
        print(f"Profile ID: {profile_id} => ", end='')
        search = chunk.loc[chunk['profile_id'] == profile_id]
        if len(search.index) == 0:
            print("profile does not have any posts")
            #return search
        else:
            print(f"{len(search.index)} posts")
            print(search)
            return search
        break

"""
Write another function that, given an input n (an integer), will return the posts that belong to the n top posted profiles (top n profiles that have posted the highest number of posts) that their data is available in the profile.csv using the previously written function.
"""

def top_profiles(n, chunksize = 5000):
    data = import_dataset_columns("instagram_posts.csv", ['profile_id', 'post_id'], chunksize)
    for chunk in data:
        sorted_data = chunk.groupby(['profile_id'])['profile_id'].count().sort_values(ascending=False).head(n)
        top_profiles = sorted_data.index.tolist()
        return top_profiles
        break

def posts_of_top_profiles(n, chunksize = 5000):
    profiles = top_profiles(n, chunksize)
    for profile in profiles:
        findPostsByProfileId(profile, chunksize)

"""
What is the average number of "likes" and comments of the top 10 profiles with the highest number of posts which their information is available 
in profile.csv?
"""
def top_profiles_average_likes_and_comments(n, chunksize = 5000):
    profiles = top_profiles(n, chunksize)
    likes = 0
    comments = 0
    for profile in profiles:
        posts = findPostsByProfileId(profile, chunksize)
        likes += posts['numbr_likes'].sum()
        comments += posts['number_comments'].sum()
    print(f"total number of likes: {likes}")
    print(f"total number of comments: {comments}")
    print(f'average of likes and comments per profile in top {n} list: {(likes+comments)/n}')

"""

"""