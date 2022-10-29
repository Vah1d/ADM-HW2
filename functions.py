#Q1 EDA

def clean(data):
    df = data.select_dtypes(include = ['number']).dropna()
    df = data.fillna(0)
    return df


#Q2

def import_dataset_columns(dataset, columns, chunksize):
    df = pd.read_csv(
        dataset, 
        delimiter='\t', 
        chunksize=chunksize, 
        usecols=[*columns])
    return(df)

def import_dataset(dataset, chunksize):
    df = pd.read_csv(
        dataset, 
        delimiter='\t', 
        chunksize=chunksize)
    return(df)
 
def n_posts(distr):
    print(distr.shape)
    plt.figure(figsize = (1100/72.,4.8))
    plt.hist(distr.tail(3400000),bins = 30, density = True)
    plt.title("Number of posts for each profile in descending order")
    plt.xlabel("number of posts")
    plt.ylabel("density of the number of profiles")
    plt.show()

def piegraph_location(no_loc,loc):
    no_loc = sum(location['binary'] == 0)
    loc = sum(location['binary'] == 1)

    size = [no_loc,loc]
    labels = ['Posts without location', 'posts with location']

    fig1, ax1 = plt.subplots(figsize = (1100/72.,4.8))
    ax1.pie(size, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')

    plt.show()


#Q7

def probQ7(distr):
    distr['20%'] = 0.2*distr['followers']
    probability = sum(distr['numbr_likes'] >= distr['20%'])/len(distr['followers'])
    print('{0:.2%} of the posts have 20% more likes than followers of the user that posted the post'.format(round(probability,3)))

#Q8

def scatter_plot(column1,column2):
    fig, ax = plt.subplots()
    ax.scatter(column1,column2)
    plt.title("scatterplot of likes & comments for each post")
    plt.xlabel("number of likes")
    plt.ylabel("number of comments")
    line = mlines.Line2D([0, 1], [0, 1], color='red')
    transform = ax.transAxes
    line.set_transform(transform)
    ax.add_line(line)
    ax.ticklabel_format(useOffset = False)
    plt.show()

def emp_distr(distribution):
    fig1, ax1 = plt.subplots(figsize = (1100/72.,4.8))

    ax1.hist(distribution.tail(4400000),bins = 100)
    plt.xlabel("number of followers")
    plt.ylabel("number of profiles")
    plt.show()    
    
def m_m_q(distribution):
    print('1. the average number of followers for an instagram account is: {}'.format(round(distribution.mean(),2)))
    print('2. the number of followers that appear the most for instagram accounts is: {}'.format(distribution.mode()[0]))
    print('3. the 10 quantiles of our distribution are:\n{}'.format(distribution.quantile(np.round(np.linspace(0,1.0,10),1))))
