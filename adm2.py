import pandas as pd
from datetime import time
import matplotlib.pyplot as plt
import csv
    
def import_dataset_columns(dataset, columns, chunksize = 5000):
    """
    description:
        Importing dataset with defined columns.
    params:
        - dataset: name of the file with data;
        - columns: list of columns to retrieve from dataset;
        - chunksize: size of dataset to compute.
    return:
        dataset in format "TextFileReader".
    """
    df = pd.read_csv(
        dataset, 
        delimiter='\t', 
        chunksize=chunksize, 
        encoding = 'ISO-8859-1', 
        usecols=[*columns])
    return df

def import_dataset(dataset, chunksize = 5000):
    """
    description:
        Importing whole dataset.
    params:
        - dataset: name of the file with data;
        - chunksize: size of dataset to compute.
    return:
        dataset in format "TextFileReader".
    """
    df = pd.read_csv(
        dataset, 
        delimiter='\t', 
        chunksize=chunksize, 
        encoding = 'ISO-8859-1')
    return df
    
def time_count_in_interval(chunk, interval):
    """
    description:
        Searching number of posts (in chunk) in defined time interval.
    params:
        - chunksize: size of dataset to compute,
        - interval: list of start and end of time interval, e.g. ['00:00:00', '01:00:00'].
    return:
        number of posts in defined time interval.
    """
    return chunk.loc[(chunk > time.fromisoformat(interval[0])) & (chunk <= time.fromisoformat(interval[1]))].count()

def common_time(chunksize = 5000):
    """
    RQ3
    description:
        1) What is the most common time in which users publish their posts?
    params:
        - chunksize: size of dataset to compute.
    output:
        the most common time interval and number of posts in that interval
    """
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

def plot_intervals_posts(intervals, chunksize = 5000):
    """
    RQ3
    description:
        2) Plot the number of posts for each given time interval.
    params:
        - intervals: list of time intervals;
        - chunksize: size of dataset to compute.
    output:
        plot with the number of posts for each given interval.
    """
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
        list(intervals_posts.values()))
    plt.xlabel("Intervals")
    plt.ylabel("Number of posts")
    plt.title("Number of posts to time intervals")

    
def findPostsByProfileId(profile_id, chunksize = 5000):
    """
    RQ4
    description:
        1) Searching the posts by user (profile_id).
    params:
        - profile_id: user profile id;
        - chunksize: size of dataset to compute.
    return:
        posts that belong to the given profile_id or message about its absence.
    """
    data = import_dataset_columns("instagram_posts.csv", 
                                  [
                                      'profile_id', 
                                      'post_id', 
                                      'post_type', 
                                      'description', 
                                      'numbr_likes',
                                      'number_comments', 
                                      'cts'
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
            #print(search)
            return search
        break

def top_profiles(n, chunksize):
    """
    description:
        Searching for top n profiles that have posted the highest number of posts.
    params:
        - n: number of top profiles;
        - chunksize: size of dataset to compute.
    return:
        list of top n profiles id.
    """
    data = import_dataset_columns("instagram_posts.csv", ['profile_id', 'post_id'], chunksize)
    for chunk in data:
        sorted_data = chunk.groupby(['profile_id'])['profile_id'].count().sort_values(ascending=False).head(n)
        top_profiles = sorted_data.index.tolist()
        return top_profiles
        break

def posts_of_top_profiles(n, chunksize = 5000):
    """
    description:
        Searching for top n profiles' posts.
    params:
        - n: number of top profiles;
        - chunksize: size of dataset to compute.
    return:
        posts of top n profiles.
    """
    profiles = top_profiles(n, chunksize)
    frames = []
    for profile in profiles:
        frames.append(findPostsByProfileId(profile, chunksize))
    return pd.concat(frames)
    
def top_profiles_average_likes_and_comments(n, chunksize = 5000):
    """
    description:
        Searching the average of likes and comments per profile in top n profiles list.
    params:
        - n: number of top profiles;
        - chunksize: size of dataset to compute.
    output:
        information about:
        - total number of likes of the top n profiles;
        - total number of comments of the top n profiles;
        - the average of likes and comments per profile in top n profiles list.
    """
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

def top_profiles_posts_by_intervals_plot(intervals, n = 10, chunksize = 1000000):
    intervals_posts = {}
    df_posts = posts_of_top_profiles(n, chunksize)
    timestamps_of_posts = df_posts['cts']
    print(timestamps_of_posts)
    for chunk in timestamps_of_posts:
        print(chunk)
        chunk = pd.to_datetime(chunk)
        print(chunk)
        
        chunk = pd.Series([val.time() for val in chunk])
        print(chunk)
        
        for interval in intervals:
            anot = interval[0]+' - '+interval[1]
            intervals_posts[anot] = time_count_in_interval(chunk, interval)
        
        break
    print(intervals_posts)
    