
import pandas as pd
#import numpy as np
#import matplotlib
#import matplotlib.pyplot as plt

#series
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print cities

print '\n'
print 'Cities Less than 1000?'
less_than_1000 = cities < 1000
print less_than_1000
print '\n'
print 'only cities L\less than 1000'
print cities[less_than_1000]



#dataframe

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
print football
football.head()

print football.describe()
print football.info()
