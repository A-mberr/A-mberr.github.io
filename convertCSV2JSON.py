# Name: Amber Nobel
# Student number: 11819359

import pandas as pd
import json

# reads csv and converts it to a dataframe
df = pd.read_csv('cereal.csv', delimiter=';')

df = df[['name', 'calories']]
print(df)

# creates json with the country as index
data = df.set_index('name').to_json(orient='table')
print(data)

# saves the KNMI_temp as a json file
with open('data.json', 'w') as outfile:
    outfile.write(data)
