# import module for handling csv files.
import csv
import lyricsgenius


# open csv files.
csv_file = open("sample Hot Stuff.csv", "r")
# read csv file as a dictionaries, you can access each dictionary by iterating
# through them.
csv_reader = csv.DictReader(csv_file)

# TODO: write a function that inputs a WeekID '6/1/1963' and output the year.


# TODO: iterate through the dictionaries and create a new dictionary as follows
# the keys are the strings of the year of the songs, and the values are lists of
# (song name, song artist).


# TODO: get the lyrics of each song and store them in a dictionary
# the keys are the strings of year of the songs, and the values are lists of
# the song lyrics.


# get the lyrics
token = "V8Opg99OuwwJOZcObVK7aKfIfloTdl-DJSvo5LMwmox5Tv5JNF-QByjyi6ff4m2i"
genius = lyricsgenius.Genius(token, verbose=False)
song = genius.search_song('Casanova', artist="Levert")
# TODO: clean up the lyrics using regex.
print(song.lyrics)
# TODO: add it to the dictionary

csv_file.close()
