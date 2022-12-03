
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('./CONTENT_INTERACTION/ViewingActivity.csv')
df = df.drop(['Profile Name', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df = df.set_index('Start Time')
df.index = df.index.tz_convert('US/Eastern')
df = df.reset_index()
df['Duration'] = pd.to_timedelta(df['Duration'])
found = df[df['Title'].str.contains('S.W.A.T', regex=False)]
found = found[(found['Duration'] > '0 days 00:01:00')]
found['weekday'] = found['Start Time'].dt.weekday
found['hour'] = found['Start Time'].dt.hour

found['weekday'] = pd.Categorical(found['weekday'], categories=
    [0,1,2,3,4,5,6],
    ordered=True)
found_by_day = found['weekday'].value_counts()
found_by_day = found_by_day.sort_index()
matplotlib.rcParams.update({'font.size': 22})
found_by_day.plot(kind='bar', figsize=(20,10), title='Episodes Watched by Day')

print(df.shape)
print(df.dtypes)
#print(df.head(1))
print(found)
print(found['Duration'].sum())
plt.savefig('foo.png')
