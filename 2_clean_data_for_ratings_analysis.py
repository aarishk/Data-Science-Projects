import pandas as pd
import numpy as np

#Creating DataFrame of IMDB Id's with only movies
df = pd.read_csv("Data/title_ratings_cleaned.gz", index_col = False, usecols=["tconst", "averageRating"])
df.dropna(inplace = True)
df = df.reset_index(drop=True)
df_idsToKeep = pd.DataFrame(columns=["tconst"])
df_idsToKeep["tconst"] = df.tconst
print("Done: Creating ids_to_keep\n")


#Creating Modified title_basics_cleaned.csv
print("Start: Reading title_basics_cleaned.gz")
df_to_modify = pd.read_csv("Data/title_basics_cleaned.gz", index_col = False)
df_to_modify = pd.merge(df_idsToKeep,df_to_modify,on=["tconst"])
df_to_modify.to_csv("Data/title_basics_for_ratings_analysis.gz", compression = "gzip", index = False)
print("Done: Creating title_basics_for_ratings_analysis.gz\n")




