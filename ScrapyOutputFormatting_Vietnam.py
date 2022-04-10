#Load Packages:
import pandas as pd

#Load scraped JSON files:
raw_1 = pd.read_json('/Users/juan/Documents/Data Science Portfolio/pythonscrapy/pythonscrapy/vietnam1.json')
raw_2 = pd.read_json('/Users/juan/Documents/Data Science Portfolio/pythonscrapy/pythonscrapy/vietnam2.json')

#Expand city_postal column:
city_postal_expanded_1 = raw_1['city_postal'].apply(pd.Series)
city_postal_expanded_2 = raw_2['city_postal'].apply(pd.Series)

#Back fill city names:
for row in range(0, city_postal_expanded_1.shape[0]):
    for col in range(0, city_postal_expanded_1.shape[1]):
        if (city_postal_expanded_1.iloc[row,col] == " "):
            city_postal_expanded_1.iloc[row,col] = city_postal_expanded_1.iloc[row,col - 2]
            
for row in range(0, city_postal_expanded_2.shape[0]):
    for col in range(0, city_postal_expanded_2.shape[1]):
        if (city_postal_expanded_2.iloc[row,col] == " "):
            city_postal_expanded_2.iloc[row,col] = city_postal_expanded_2.iloc[row,col - 2]

#Create list of dictionaries for city_postal_expanded_1:
list_1 = []

for row in range(0, city_postal_expanded_1.shape[0]):
    for col in range(0, city_postal_expanded_1.shape[1],2):
        dict_1 = {}
        dict_1['row_index'] = city_postal_expanded_1.index[row]
        dict_1['city'] = city_postal_expanded_1.iloc[row,col]
        dict_1['zipcode'] = city_postal_expanded_1.iloc[row,col+1]
        list_1.append(dict_1)

#Convert list of dictionaries to dataframe:        
df_1 = pd.DataFrame(list_1)

#Create list of dictionaries for city_postal_expanded_2:
list_2 = []

for row in range(0, city_postal_expanded_2.shape[0]):
    for col in range(0, city_postal_expanded_2.shape[1],2):
        dict_2 = {}
        dict_2['row_index'] = city_postal_expanded_2.index[row]
        dict_2['city'] = city_postal_expanded_2.iloc[row,col]
        dict_2['zipcode'] = city_postal_expanded_2.iloc[row,col+1]
        list_2.append(dict_2)

#Convert list of dictionaries to dataframe:         
df_2 = pd.DataFrame(list_2)

#Subset raw data with columns of interest:
home_1 = raw_1[['country', 'subregion', 'province', 'district']]

#Convert list columns to strings:
home_1['country'] = home_1['country'].str[0]
home_1['subregion'] = home_1['subregion'].str[0]
home_1['province'] = home_1['province'].str[0]
home_1['district'] = home_1['district'].str[0]

#Convert the index into a column:
home_1.reset_index(inplace = True)

#Rename the index:
home_1.rename(columns = {'index': 'row_index'}, inplace = True)

#Merge dataframes:
df_1 = df_1.merge(home_1, on = 'row_index', how = 'left')

#Sort dataframe by State and City:
df_1 = df_1.sort_values(by = ['subregion', 'province','district', 'city'])

#Drop and rows where the zipcode is nan:
df_1.dropna(subset = ['zipcode'], inplace = True)

#Drop the row index column:
df_1.drop(['row_index'], inplace = True, axis = 1)

#Subset raw data with columns of interest:
home_2 = raw_2[['country', 'subregion', 'province']]

#Convert list columns to strings:
home_2['country'] = home_2['country'].str[0]
home_2['subregion'] = home_2['subregion'].str[0]
home_2['province'] = home_2['province'].str[0]

#Add district column as blank:
home_2['district'] = ''

#Convert the index into a column:
home_2.reset_index(inplace = True)

#Rename the index:
home_2.rename(columns = {'index': 'row_index'}, inplace = True)

#Merge dataframes:
df_2 = df_2.merge(home_2, on = 'row_index', how = 'left')

#Sort dataframe by State and City:
df_2 = df_2.sort_values(by = ['subregion', 'province','district', 'city'])

#Drop any rows where the zipcode is nan:
df_2.dropna(subset = ['zipcode'], inplace = True)

#Drop the row index column:
df_2.drop(['row_index'], inplace = True, axis = 1)

df = df_1.append(df_2,ignore_index = True)

#Export dataframe to csv file:
df.to_csv('/Users/juan/Documents/Data Science Portfolio/pythonscrapy/vietnam_data.csv', index=False)
