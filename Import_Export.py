# Python script to read and edit Import & Export Global data

import pandas as pd

filename = "C:/Users/MagalJor/Documents/Python Scripts/Import_Export/BACI_HS17_Y2020_V202201.csv"

df = pd.read_csv(filename)  # Original file loaded into Python

#  Change names of columns
df.rename(columns={"t": "Year", "i": 'Exporter', "j": 'Importer', "k": "Product", "v": "Value", "q": "Quantity"},
          inplace=True)

# print(df)

#  Country list
countries = [24, 32, 36, 56, 76, 120, 124, 152, 156, 170, 188, 218, 251, 276, 288, 360, 372, 381, 392, 404, 410, 458,
             484, 528, 566, 604, 608, 616, 690, 699, 704, 710, 724, 764, 792, 800, 826, 834, 842
             ]

#  Country lists by region

africa = [24, 120, 288, 404, 566, 690, 710, 800, 834]
apac = [36, 360, 410, 458, 608, 704, 764]
europe = [251, 372, 724, 792]
latam = [32, 76, 152, 170, 188, 218, 484, 604]
nam = [124, 842]
china = [156]
india = [699]
UK = [826]
germany = [276]

#  Generate importer dataframes by region

df_africa_importer = df[df['Importer'].isin(africa)]
df_apac_importer = df[df['Importer'].isin(apac)]
df_europe_importer = df[df['Importer'].isin(europe)]
df_latam_importer = df[df['Importer'].isin(latam)]
df_nam_importer = df[df['Importer'].isin(nam)]
df_china_importer = df[df['Importer'].isin(china)]
df_india_importer = df[df['Importer'].isin(india)]
df_UK_importer = df[df['Importer'].isin(UK)]
df_germany_importer = df[df['Importer'].isin(germany)]


#  Generate exporter dataframes by region

df_africa_exporter = df[df['Exporter'].isin(africa)]
df_apac_exporter = df[df['Exporter'].isin(apac)]
df_europe_exporter = df[df['Exporter'].isin(europe)]
df_latam_exporter = df[df['Exporter'].isin(latam)]
df_nam_exporter = df[df['Exporter'].isin(nam)]
df_china_exporter = df[df['Exporter'].isin(china)]
df_india_exporter = df[df['Exporter'].isin(india)]
df_UK_exporter = df[df['Exporter'].isin(UK)]
df_germany_exporter = df[df['Exporter'].isin(germany)]

#print("Africa", df_africa)
#print("APAC", df_apac)
#print("Europe", df_europe)
#print("LATAM", df_latam)
#print("NAM", df_nam)

#  Create importer csv files

df_africa_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_africa_importer.csv", index=False)
df_apac_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_apac_importer.csv", index=False)
df_europe_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_europe_importer.csv", index=False)
df_latam_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_latam_importer.csv", index=False)
df_nam_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_nam_importer.csv", index=False)
df_china_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_china_importer.csv", index=False)
df_india_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_india_importer.csv", index=False)
df_UK_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_UK_importer.csv", index=False)
df_germany_importer.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_germany_importer.csv", index=False)

#  Create exporter csv files

df_africa_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_africa_exporter.csv", index=False)
df_apac_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_apac_exporter.csv", index=False)
df_europe_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_europe_exporter.csv", index=False)
df_latam_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_latam_exporter.csv", index=False)
df_nam_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_nam_exporter.csv", index=False)
df_china_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_china_exporter.csv", index=False)
df_india_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_india_exporter.csv", index=False)
df_UK_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_UK_exporter.csv", index=False)
df_germany_exporter.to_csv("C:/Users/MagalJor/Documents/Python Scripts/Import_Export/df_germany_exporter.csv", index=False)