__author__ = 'pankils'

import pandas as pd
import numpy as np

data = pd.read_csv('unemploymentdata.csv')

data['Series ID'] = ['Labor force', 'Participation rate','Rate', 'Rate - 16-19 yrs','Rate - 20+ yrs (Men)','Rate - 20+ yrs (Women)','Rate - White','Rate - Black or African American','Rate - Asian',
'Rate - Hispanic or Latino','No High School Diploma','High School Graduates','Some College or Associate Degree','Bachelor degree and higher','Under 5 Weeks','5-14 Weeks', '15 Weeks & over', '27 Weeks & over']


print data.head(5)

print data.drop(['Jan 2000','Sep 2015','Oct 2015','Nov 2015','Dec 2015'], axis=1, inplace=True)
data.set_index('Series ID', inplace=True)
data= data.transpose().convert_objects(convert_numeric=True)
data[['Rate - Asian','Rate - White','Rate - Black']].plot()
data['Year'] = (data.index.to_datetime()).year #extracting year
years = data.groupby('Years') #group by year
years['Rate'].mean().plot(kind='bar') #plotting by year
years['Rate'].agg([np.mean,np.std,min,max])


