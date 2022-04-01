# Python script to read and edit Import & Export Global data

import pandas as pd

filename = "C:/Users/MagalJor/Documents/Python Scripts/Import_Export/BACI_HS17_Y2020_V202201.csv"

df = pd.read_csv(filename)  # Original file loaded into Python

#  Change names of columns
df.rename(columns={"t": "Year", "i": 'Exporter', "j": 'Importer', "k": "Product", "v": "Value", "q": "Quantity"},
          inplace=True)

# print(df)

#  Country selected in this case Indonesia
country = [690]

#  Generate importer dataframe

df_seychelles_importer = df[df['Importer'].isin(country)]

#  Generate exporter dataframe

df_seychelles_exporter = df[df['Exporter'].isin(country)]


#  Create importer csv file

df_seychelles_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_seychelles_importer.csv", index=False)

#  Create exporter csv file

df_seychelles_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_seychelles_exporter.csv", index=False)