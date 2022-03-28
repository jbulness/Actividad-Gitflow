def top_10_retweeted(df):
    return df.sort_values(by=['retweetCount'], ascending=False).head(10)