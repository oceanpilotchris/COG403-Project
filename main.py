# import module for handling csv files.
import csv
from typing import List, Dict
import lyricsgenius
import re

# open csv files.
csv_file = open("sample Hot Stuff.csv", "r")
# read csv file as a dictionaries, you can access each dictionary by iterating
# through them.
csv_reader = csv.DictReader(csv_file)
lines = sum(1 for row in csv_reader)
csv_file.seek(0)


# A bunch of basic getters
def get_week_ids() -> list:
    csv_file.seek(0)
    week_ids = []
    for songs in csv_reader:
        week_ids.append(songs["WeekID"])
    return week_ids


def get_song_names() -> list:
    csv_file.seek(0)
    song_names = []
    for songs in csv_reader:
        song_names.append(songs["Song"])
    return song_names


def get_performers() -> list:
    csv_file.seek(0)
    performers = []
    for songs in csv_reader:
        performers.append(songs["Performers"])
    return performers


def get_year_published(week_id: str) -> int:
    """
    This function that inputs a WeekID '6/1/1963' and output the year.
    :param week_id: "WeekID" of a song in Hot Stuff.csv
    :return: int for of the year
    """
    l = len(week_id)
    return int(week_id[l - 4: l])

# TODO: iterate through the dictionaries and create a new dictionary as follows
# the keys are the strings of the year of the songs, and the values are lists of
# (song name, song artist).
# step 1:
def get_i_by_year(first_year: int, last_year: int) -> List[int]:
    """
    Extracts songs from first_year-last_year and return them by their index in Hot Stuff.csv
    :param first_year: the first year to be included
    :param last_year: the last year to be included. last_year >= first_year
    :return: a list of the desired songs' index in Hot Stuff
    """
    indexes = []
    for i in range(lines):
        if first_year <= get_year_published(get_week_ids()[i]) <= last_year:
            indexes.append(i)
    return indexes
# print(get_week_ids())
# print(get_i_by_year(2008, 2019))
# song_info = {}
#
#
# print(song_info)
# step 2: create the desired dictionary


# TODO: get the lyrics of each song and store them in a dictionary
# the keys are the strings of year of the songs, and the values are lists of
# the song lyrics.


# get the lyrics
token = "V8Opg99OuwwJOZcObVK7aKfIfloTdl-DJSvo5LMwmox5Tv5JNF-QByjyi6ff4m2i"
genius = lyricsgenius.Genius(token, verbose=False)
song = genius.search_song('California Gurls', artist="Katy Perry Featuring Snoop Dogg")
# TODO: clean up the lyrics using regex.
lyrics = re.sub("\n", " ", song.lyrics)
# print(song.lyrics)
# TODO: add it to the dictionary

csv_file.close()
