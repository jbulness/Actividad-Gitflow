import pandas as pd

def top_10_users(tweets):
    usernames = []
    for tweet in tweets:
        usernames.append(tweet["user"]["username"])
    df2 = pd.DataFrame(usernames, columns=["username"])

    #https://stackoverflow.com/questions/40454030/count-and-sort-with-pandas
    return df2.groupby(['username'])['username'].count().reset_index(name='number_of_tweets').sort_values(['number_of_tweets'], ascending=False).head(10)

