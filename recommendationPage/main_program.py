import pandas as pd
import numpy as np
import random
import requests
import json




# our main movie data








    #example imput from user data

def mainP(input_movies):
    dm=pd.read_csv('recommendationPage/movie_data.csv')                      # movie database
    dm=dm.iloc[:,1:]


    df=pd.DataFrame.from_dict(input_movies, orient='index')
    df=df.reset_index()
    df.columns=['title','input_rating']
    df['input_rating']=df['input_rating'].astype(int)

    di = pd.DataFrame(df)# input data in the form of title,rating






    # prepaing three lists of years for proper timescale selections

    list_1=[2008.0, 2009.0, 2010.0, 2011.0, 2012.0, 2013.0, 2014.0, 2015.0, 2016.0, 2017.0, 2018.0]
    list_2=[2000.0, 2001.0, 2002.0, 2003.0, 2004.0, 2005.0, 2006.0, 2007.0]
    list_3=[1995.0, 1994.0, 1996.0, 1976.0, 1992.0, 1988.0, 1967.0, 1993.0, 1964.0, 1977.0, 1965.0, 1982.0, 1985.0, 1990.0, 1991.0, 1989.0, 1937.0, 1940.0, 1969.0, 1981.0, 1973.0, 1970.0, 1960.0, 1955.0, 1959.0, 1968.0, 1980.0, 1975.0, 1986.0, 1948.0, 1943.0, 1950.0, 1946.0, 1987.0, 1997.0, 1974.0, 1956.0, 1958.0, 1949.0, 1972.0, 1998.0, 1933.0, 1952.0, 1951.0, 1957.0, 1961.0, 1954.0, 1934.0, 1944.0, 1963.0, 1942.0, 1941.0, 1953.0, 1939.0, 1947.0, 1945.0, 1938.0, 1935.0, 1936.0, 1926.0, 1932.0, 1979.0, 1971.0, 1978.0, 1966.0, 1962.0, 1983.0, 1984.0, 1931.0, 1922.0, 1999.0, 1927.0, 1929.0, 1930.0, 1928.0, 1925.0, 1914.0, 1919.0, 1923.0, 1920.0, 1918.0, 1921.0, 1924.0, 1915.0, 1916.0, 1917.0, 1902.0, 1903.0, 1912.0, 1913.0, 1898.0, 1894.0, 1896.0, 1910.0, 1895.0, 1900.0, 1908.0, 1897.0, 1911.0, 1909.0, 1899.0, 1901.0]

    list_1=random.choices(list_1,k=3)        # list ( current to 2008)
    list_2=random.choices(list_2,k=2)        # list ( 2007 to 2000 )
    list_3=random.choices(list_3,k=1)



    # adding genres to our input data

    df=di.merge(dm,how='inner',left_on='title',right_on='title')
    df=pd.DataFrame(df)

    #building profile

    profile=df.drop('title',axis=1).drop('movieId',axis=1).drop('year',axis=1).drop('genres',axis=1).drop('imdbId',axis=1).drop('tmdbId',axis=1)
    profile=profile.transpose().dot(profile['input_rating'])




    # dividing movie data sets into 3 datas according to thier year list : [list1,list2,list3]

    d1=dm[dm['year'].isin(list_1)]
    d1=d1.drop('title',axis=1).drop('year',axis=1).drop('genres',axis=1).drop('tmdbId',axis=1).drop('imdbId',axis=1)
    d1=d1.set_index(d1['movieId']).iloc[:,1:]


    d2=dm[dm['year'].isin(list_2)]
    d2=d2.drop('title',axis=1).drop('year',axis=1).drop('genres',axis=1).drop('tmdbId',axis=1).drop('imdbId',axis=1)
    d2=d2.set_index(d2['movieId']).iloc[:,1:]



    d3=dm[dm['year'].isin(list_3)]
    d3=d3.drop('title',axis=1).drop('year',axis=1).drop('genres',axis=1).drop('tmdbId',axis=1).drop('imdbId',axis=1)
    d3=d3.set_index(d3['movieId']).iloc[:,1:]





    #similar movie score

    d1=((d1*profile).sum(axis=1))/(profile.sum())
    d1=d1.sort_values(ascending=False)
#     print(d1.head)



    d2=((d2*profile).sum(axis=1))/(profile.sum())
    d2=d2.sort_values(ascending=False)


    d3=((d3*profile).sum(axis=1))/(profile.sum())
    d3=d3.sort_values(ascending=False)



    imdbId=[]

    #recommeded movie list
    ids=d1.head(5)
    ids=pd.DataFrame(ids).reset_index()
    d=dm.merge(ids,how='inner',left_on='movieId',right_on='movieId')
    imdbId.extend(list(d['imdbId']))

    ids=d2.head(3)
    ids=pd.DataFrame(ids)
    d=dm.merge(ids,how='inner',left_on='movieId',right_on='movieId')
    imdbId.extend(list(d['imdbId']))

    ids=d3.head(2)
    ids=pd.DataFrame(ids)
    d=dm.merge(ids,how='inner',left_on='movieId',right_on='movieId')
    imdbId.extend(list(d['imdbId']))

    print(imdbId)

    #api credentials
    headers={
        #enter your api headers obtained from api website
    }


    movie_details={}

    k=0
    for i in imdbId:

        #api search by id
        response = requests.get("https://movie-database-imdb-alternative.p.rapidapi.com/?i="+i+"&r=json",headers=headers)
        response=response.json()

        # keep here conditions for your various fiter selections like language, country, length,etc.

        lst=[]

        lst.append(response['Poster'])
        lst.append(response['Title'].upper())
        lst.append(response['Year'])
        lst.append(response['Director'])
        lst.append(response['Actors'])
        lst.append(response['Runtime'])
        lst.append(response['Plot'])
        lst.append(response['Language'])
        movie_details[k]=lst
        k+=1

    print(movie_details)

    return movie_details
