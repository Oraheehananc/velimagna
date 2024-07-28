import pandas as pd

# Sample data
data = {
    'PostSpon': ['user1', 'user2', 'user3', 'user4'],
    'PosterID': ['user1', 'userX', 'user3', 'userY']
}

df_ad = pd.DataFrame(data)

# Create new column based on condition
df_ad['NewColumn'] = df_ad.apply(lambda row: '@' + row['PostSpon'] if row['PostSpon'] == row['PosterID'] else None, axis=1)

print(df_ad)
