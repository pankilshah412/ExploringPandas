

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('http://files.grouplens.org/datasets/movielens/ml-100k/u.user', sep='|', names=u_cols)
#print users.head()

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('http://files.grouplens.org/datasets/movielens/ml-100k/u.data', sep='\t', names=r_cols)
#print ratings.head()

m_cols = ['movie_id', 'title', 'release_date','video_release_date', 'imdb_url']
movies = pd.read_csv('http://files.grouplens.org/datasets/movielens/ml-100k/u.item', sep='|', names=m_cols, usecols=range(5))
#print movies.head()
#print movies.info()
#print movies.dtypes
#users.describe()
#by_occupation= users.groupby('occupation')

movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)
most_rated = lens.groupby('title').size().order(ascending=False)[:25]
print 'Most rated movies' , most_rated

grouped_data = lens['rating'].groupby(lens['title']).mean().order(ascending=False) # gives average rating per movie in descending
#print grouped_data
max_ratings = grouped_data.max() # returns maximum rating number
good_movie_ids = grouped_data[grouped_data == max_ratings].index #filtering movies with highest rating
print 'Movies with highest rating\n', lens[lens.title.isin(good_movie_ids)].title.drop_duplicates() #filtering and drop duplicates
print '\n'
#or

movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
movie_stats.head()
atleast_100 = movie_stats['rating']['size'] >= 100
print 'Movies with atleast 100 ratings and highest ratings',movie_stats[atleast_100].sort([('rating', 'mean')], ascending=False)[:15] # or grouped_data[atleast_100][:15]

labels = ['0-9', '10-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79']
lens['age_group'] = pd.cut(lens.age, range(0, 81, 10), right=False, labels=labels)
print lens[['age', 'age_group']].drop_duplicates()[:10]
print lens.groupby('age_group').agg({'rating': [np.size, np.mean]})

most_50 = lens.groupby('movie_id').size().order(ascending=False)[:50]
print most_50
print lens.index
lens.set_index('movie_id', inplace=True)
by_age = lens.ix[most_50.index].groupby(['title', 'age_group'])
by_age.rating.mean().head(15)
by_age.rating.mean().unstack(1).fillna(0)[10:20]
lens.reset_index('movie_id', inplace=True)

pivoted = lens.pivot_table(index=['movie_id','title'],
                           columns=['sex'],
                           values='rating',
                           fill_value=0)
pivoted.head()
pivoted['diff'] = pivoted.M - pivoted.F
pivoted.head()

pivoted.reset_index('movie_id', inplace=True)

disagreements = pivoted[pivoted.movie_id.isin(most_50.index)]['diff']
disagreements.order().plot(kind='barh', figsize=[9, 15])
plt.title('Male vs. Female Avg. Ratings\n(Difference > 0 = Favored by Men)')
plt.ylabel('Title')
plt.xlabel('Average Rating Difference')

users.age.hist(bins=30)
plt.title("Distribution of users' ages")
plt.ylabel('count of users')
plt.xlabel('age')




