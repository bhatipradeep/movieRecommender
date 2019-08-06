from django.shortcuts import render
import pandas as pd
import random
import numpy as np
from recommendationPage.main_program import mainP
import requests




# input movie list for taking ratings from user
movie_names=['Se7en','Inception','Arrival',"""Don't Breathe""","A Quiet Place",'Escape Plan: The Extractors','Truth or Dare','Die hard','The Dictator','The Matrix Revisited','Toy Story','Slumdog Millionaire','21 Jump Street',"Men in Black",'Interstellar','Terminator 2: Judgment Day']


#manually adding image source for input movies for getting ratings of user
img=['https://m.media-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjcyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BZGI5ZTU2M2YtZWY4MC00ZDFhLTliYTItZTk1NjdlN2NkMzg2XkEyXkFqcGdeQXVyMjY5ODI4NDk@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BMjI0MDMzNTQ0M15BMl5BanBnXkFtZTgwMTM5NzM3NDM@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BMDQ2ZjUxMGUtMDg1Yy00ZWE4LWIyZTMtNThiN2IwZmE4ZDVkXkEyXkFqcGdeQXVyOTg4MDYyNw@@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BOGU2YTZmMjYtZDUwYi00NTc1LTlkMjAtM2ViZDkzOTlhNGNhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BZjRlNDUxZjAtOGQ4OC00OTNlLTgxNmQtYTBmMDgwZmNmNjkxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BNTlkOWYzZDYtNzQ1MS00YTNkLTkyYTItMjBmNjgyMDBlMjI4XkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BMTIzMTA4NDI4NF5BMl5BanBnXkFtZTYwNjg5Nzg4._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BZmNjZWI3NzktYWI1Mi00OTAyLWJkNTYtMzUwYTFlZDA0Y2UwXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BMTc3NzQ3OTg3NF5BMl5BanBnXkFtZTcwMjk5OTcxNw@@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BOTlhYTVkMDktYzIyNC00NzlkLTlmN2ItOGEyMWQ4OTA2NDdmXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg',
 'https://m.media-amazon.com/images/M/MV5BMGU2NzRmZjUtOGUxYS00ZjdjLWEwZWItY2NlM2JhNjkxNTFmXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg']



# Create your views here.

def input(request):

    if request.method=='POST':
        dict={}
        dict[movie_names[0]] = request.POST.get("movie_0")
        dict[movie_names[1]] = request.POST.get("movie_1")
        dict[movie_names[2]] = request.POST.get("movie_2")
        dict[movie_names[3]] = request.POST.get("movie_3")
        dict[movie_names[4]] = request.POST.get("movie_4")
        dict[movie_names[5]] = request.POST.get("movie_5")
        dict[movie_names[6]] = request.POST.get("movie_6")
        dict[movie_names[7]] = request.POST.get("movie_7")
        dict[movie_names[8]] = request.POST.get("movie_8")
        dict[movie_names[9]] = request.POST.get("movie_9")
        dict[movie_names[10]] = request.POST.get("movie_10")
        dict[movie_names[11]] = request.POST.get("movie_11")
        dict[movie_names[12]] = request.POST.get("movie_12")
        dict[movie_names[13]] = request.POST.get("movie_13")
        dict[movie_names[14]] = request.POST.get("movie_14")
        dict[movie_names[15]] = request.POST.get("movie_15")


        input_movies={}
        #transfering only rated movies to input_movies
        for k in dict.keys():
            try:
                if len(dict[k])>0:
                    input_movies[k]=dict[k]
            except:
                pass

        #sending to out main program
        rmovies=mainP(input_movies)
        return render(request,'recommendOut.html',{'details':rmovies})







    return render(request,'recommendIn.html',{'images': img,'movies': movie_names })
