def top_10_hashtags(df):
    # Función basada en el código obtenido del siguiente link: https://stackoverflow.com/questions/63228403/count-hashtag-frequency-in-a-dataframe 
    return df['content'].str.findall(r'(#\w+)').explode().value_counts()
