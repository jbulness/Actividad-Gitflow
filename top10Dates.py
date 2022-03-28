import pandas as pd

def top_10_dates(tweets):
    dates = []
    for tweet in tweets:
        day=tweet["date"].split("T")[0]
        dates.append(day)
    df3 = pd.DataFrame(dates, columns=["days"])

    # Función basada en el código del siguiente link: https://stackoverflow.com/questions/40454030/count-and-sort-with-pandas
    return df3.groupby(['days'])['days'].count().reset_index(name='number_of_tweets').sort_values(['number_of_tweets'], ascending=False).head(10)
