import pandas as pd

data = pd.read_html('https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551', header=0)
df = data[0]

# since we only have 4 columns to swap,and there is no use later for the first one, we drop it
df = df.drop(columns=[df.columns[0]])

print(data)
# change required column names 
df.columns = ['TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']
print("Column names changed:")
print(df.columns)
print()

# number of individual artists
print(f"Number of individual artists: {df['ARTYSTA'].nunique()}")
print()

# most frequent artists
ten_most_frequent_artists = df['ARTYSTA'].value_counts().head(10)
top_artists = ten_most_frequent_artists[ten_most_frequent_artists == ten_most_frequent_artists.max()]
print("Most frequent artists:")
print(top_artists)
print()

# change column names to capitalized
df.columns = df.columns.str.title()
print("Column names capitalized:")
print(df.head(1))
print()

# drop the 'Max Poz' column
df = df.drop(columns=['Max Poz'])
print("Column 'Max Poz' dropped:")
print(df.head(1))
print()

# year or years with the most albums released
record_years_list_decending = df['Rok'].value_counts()
record_years= record_years_list_decending[record_years_list_decending == record_years_list_decending.max()]
print("Year(s) with the most albums released:")
print(f"{record_years}")
print()

# number of albums released between 1960 and 1990
number_of_albums = df['Rok'].between(1960, 1990).sum()
print(f"Number of albums released between 1960 and 1990: {number_of_albums}")
print()

# year of the youngest album
youngest_album_year = df['Rok'].max()
print(f"Year of the youngest album: {youngest_album_year}")
print()

# earliest released album for each artist
earliest_albums = df.sort_values('Rok').groupby('Artysta').first().reset_index()
print(earliest_albums[['Artysta', 'Tytuł', 'Rok']])

# 10. save to CSV
earliest_albums.to_csv('earliest_albums.csv', index=False, encoding='utf-8')