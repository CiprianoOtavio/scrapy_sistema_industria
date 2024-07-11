from src.beautifulsoup_request import getNewsData
from src.googlesearch_gnews import with_gnews, with_google_news_feed
import pandas as pd

sistema_industria = pd.DataFrame()

def save_dataframe(news):
    df = pd.DataFrame(news)
    return df

queries = ["SENAI PB", "IEL PB", "FIEPB", "SESI PB"]
arquivamento = ["SENAIPB", "IELPB", "FIEPB", "SESIPB"]
#SESI PB, FIEPB PB, SENAI PB, IEL PB

# news = getNewsData(query, 50)

# news = with_gnews(query)

for i in range(len(queries)):
    news = with_google_news_feed(queries[i])
    df = save_dataframe(news)
    df.to_csv(f'{arquivamento[i]}.csv', index=False)

    sistema_industria = pd.concat([sistema_industria, df])

sistema_industria.to_csv('sistema_industria.csv', index=False)