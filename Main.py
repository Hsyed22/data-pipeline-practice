import pandas as pd
import numpy as np
import requests
from fastapi import FastAPI
import requests

#Lets build an anime pipeline

def anime():
    url = f'https://api.jikan.moe/v4/anime'
    response = requests.get(url)
    if response.status_code == 200:
        print('yes')
        char_data = response.json()
        return char_data


final_char = anime()
print(final_char)


df = pd.json_normalize(final_char['data'])
df.info()
df.describe()

print(df.describe())
print(df.info())

cols = [
    "images.jpg.image_url",
    "images.jpg.small_image_url",
    "images.jpg.large_image_url",
    "images.webp.image_url",
    "images.webp.small_image_url",
    "images.webp.large_image_url",
    "trailer.youtube_id",
    "trailer.url",
    "trailer.embed_url",
    "trailer.images.image_url",
    "trailer.images.small_image_url",
    "trailer.images.medium_image_url",
    "trailer.images.large_image_url",
    "trailer.images.maximum_image_url",
    "aired.from",
    "aired.to",
    "aired.prop.from.day",
    "aired.prop.from.month",
    "aired.prop.from.year",
    "aired.prop.to.day",
    "aired.prop.to.month",
    "aired.prop.to.year",
    "aired.string",
    "broadcast.day",
    "broadcast.time",
    "broadcast.timezone",
    "broadcast.string"
]

def remove_cols(df, column):
    return df.drop(columns = column, errors = 'ignore') 

def top_score(df,score):
    return df[df['score'] >= score].reset_index(drop=True)

def agg(df,vals,aggr):
    df.groupby()

df_anime = remove_cols(df, cols)
df_anime = top_score(df_anime,7.5)




print(df_anime.info())