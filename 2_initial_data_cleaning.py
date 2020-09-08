import pandas as pd
import numpy as np

#Creating DataFrame of IMDB Id's with only movies
df = pd.read_csv("Data/title.basics.tsv.gz", sep="\t", index_col=False, usecols=["tconst", "titleType"], na_values=["\\N"], keep_default_na = True)
df.dropna(subset=["titleType"],inplace = True)
df = df[df["titleType"].str.contains("movie")]
df = df.reset_index(drop=True)
df_idsToKeep = pd.DataFrame(columns=["tconst"])
df_idsToKeep["tconst"] = df.tconst
print("Done: Creating ids_to_keep\n")

#Creating Modified title.basics.tsv.gz
print("Start: Reading title.basics.tsv.gz")
df_to_modify = pd.read_csv("Data/title.basics.tsv.gz",sep="\t", index_col=False, low_memory=False, na_values=["\\N"], keep_default_na = True, usecols=["tconst", "titleType","originalTitle","isAdult", "startYear", "runtimeMinutes", "genres"])
df_to_modify = pd.merge(df_idsToKeep,df_to_modify,on=["tconst"])
df_to_modify.to_csv("Data/title_basics_cleaned.gz", compression = "gzip", index=False)
print("Done: Creating title_basics_cleaned.gz\n")


#Creating Modified title.ratings.tsv.gz
print("Start: Reading title.ratings.tsv.gz")
df_to_modify = pd.read_csv("Data/title.ratings.tsv.gz",sep="\t", index_col=False, low_memory=False, na_values=["\\N"], keep_default_na = True)
df_to_modify = pd.merge(df_idsToKeep,df_to_modify,on=["tconst"])
df_to_modify.to_csv("Data/title_ratings_cleaned.gz", compression = "gzip", index=False)
print("Done: Creating title_ratings_cleaned.gz\n")





