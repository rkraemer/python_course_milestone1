'''
Created on 15.03.2020
Milestone Project 1: Movie Project
@author: rkraemer
'''

import json
import os.path
from os import path
#from pprint import pprint
# import only system from os
from os import system, name


movies = []

movie_properties =['name', 'director', 'year', 'rating']


MENUE_TEXT = "\n Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: "
MOVIE_FILE = "movies.json"

# define our clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    print ("Movie File exists: "+str(path.exists(MOVIE_FILE)))
    clear()

if __name__== "__main__":
    main()


# create file if not exist
if path.exists(MOVIE_FILE):
    # load the saved movies to the internal variable
    with open(MOVIE_FILE, 'r', encoding='utf-8') as data_file:
        movies = json.load(data_file)
else:
    f = open(MOVIE_FILE, "x", encoding='utf-8')


# Search movies
def search_movie():
    find_by = input("What property of the movie is that? ").lower()
    if find_by not in movie_properties:
        str_properties = ', ' .join(movie_properties)
        print(f'The property {find_by} does not exist!')
        print(f'Available properties: \n {str_properties}')
    else:
        looking_for = input("What are you looking for? ")
        found_movies = find_movie(looking_for, lambda x: x[find_by])
        #print(movie or 'No movies found.')
        if found_movies:
            if len(found_movies) >= 1:
                show_movies(found_movies)
            else:
                show_movie_details(found_movies)
        else:
            print('No movies found.')


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    rating = input("Rate the movie with *(1-4): ")

    movies.append({
        'name': name,
        'director': director,
        'year': year,
        'rating': rating
    })

    save_movies()


def show_movies(movielist=movies):
    for movie in movielist:
        show_movie_details(movie)


def show_movie_details(movie):
    print('-' * 45)
    print(f"Movie Name:  \t{movie['name']}, released in {movie['year']} ")
    print(f"Director: \t{movie['director']}")
    #print(f"Release year: {movie['year']}")
    print(f"Rating: \t{movie['rating']}")


def find_movie(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return found


def save_movies():
    mjson = json.dumps(movies)
    f = open(MOVIE_FILE,"w")
    f.write(mjson)
    f.close()


user_options = {
    'a': add_movie,
    'f': search_movie,
    'l': show_movies
    }


def menu():
    user_choice = input(MENUE_TEXT)
    while user_choice != 'q':

        if user_choice in user_options:
            selcted_function = user_options[user_choice]
            selcted_function()
        else:
            print('Unknown command, please try again.')
        user_choice = input(MENUE_TEXT)


menu()
