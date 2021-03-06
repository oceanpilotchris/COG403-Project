# import module for handling csv files.
import csv
from typing import List, Dict
import lyricsgenius
import re



# output = "lyrics2012.csv"
# desired_years = [2012]

output = "lyrics.csv"
desired_years = list(range(2008, 2019+1))





# open csv files.
csv_file = open("Hot Stuff.csv", "r", encoding='utf-8')
# read csv file as a dictionaries, you can access each dictionary by iterating
# through them.
csv_reader = csv.DictReader(csv_file)

length = 0
week_ids = []
song_names = []
performers = []
for songs in csv_reader:
    week_ids.append(songs["WeekID"])
    song_names.append(songs["Song"])
    performers.append(songs["Performer"])
    length += 1

def get_year_published(week_id: str) -> int:
    """
    This function that inputs a WeekID '6/1/1963' and output the year.
    :param week_id: "WeekID" of a song in Hot Stuff.csv
    :return: int for of the year
    """
    l = len(week_id)
    return int(week_id[l - 4: l])

# Iterate through the dictionaries and create a new dictionary as follows
# The keys are the strings of the year of the songs, and the values are lists of
# (song name, song artist).
def get_i_by_year(first_year: int, last_year: int) -> List[int]:
    """
    Extracts songs from first_year-last_year and return them by their index in Hot Stuff.csv
    :param first_year: the first year to be included
    :param last_year: the last year to be included. last_year >= first_year
    :return: a list of the desired songs' index in Hot Stuff
    """
    indexes = []
    for i in range(length):
        if first_year <= get_year_published(week_ids[i]) <= last_year:
            indexes.append(i)
    return indexes
# print(length)
# print(week_ids)
# print(get_i_by_year(2008, 2019))

def get_year_song_performer(indexes: List[int]) -> Dict:
    """
    Gets a dict of songs from the desired years for further processing in lyricsgenius
    :param indexes: the desired songs' indexes from the csv file
    :return: a dict with year as the key and list of (song name, song artist) as values.
    """
    d = {}
    for i in indexes:
        year = get_year_published(week_ids[i])
        if year not in d:
            d[year] = []
        song_name = song_names[i]
        performer = performers[i]
        if (song_name, performer) not in d[year]:
            d[year].append((song_name, performer))
    return d
# print(get_year_song_performer(get_i_by_year(2008, 2019)))

# TODO: get the lyrics of each song and store them in a dictionary
# the keys are the strings of year of the songs, and the values are lists of
# the song lyrics.
#desired_years = list(range(2008, 2019+1))


# get the lyrics
token = "V8Opg99OuwwJOZcObVK7aKfIfloTdl-DJSvo5LMwmox5Tv5JNF-QByjyi6ff4m2i"
genius = lyricsgenius.Genius(token, verbose=False, timeout=15, retries=3)

counter = 1
year2lyrics = {}
for year in desired_years:
    year2lyrics[year] = []
    if year in get_year_song_performer(get_i_by_year(2008, 2019)):
        song_infos = get_year_song_performer(get_i_by_year(2008, 2019))[year]
        for song_info in song_infos:
            song = genius.search_song(song_info[0], artist=song_info[1])
            # song = genius.search_song('California Gurls', artist="Katy Perry Featuring Snoop Dogg")
            if song is not None:
                print("processing song " + str(counter) + " : " + song_info[0])
                # TODO: clean up the lyrics using regex.
                lyrics = re.sub("\n", " ", song.lyrics)
                lyrics = re.sub(r'\[(.*?)\]', "", lyrics)
                year2lyrics[year].append(lyrics)
                counter += 1


try:
    with open(output, 'w', encoding='utf-8') as output:
        writer = csv.writer(output)
        for key, value in year2lyrics.items():
            writer.writerow([key, value])
except IOError:
    print("I/O error")

output.close()
csv_file.close()
print("all done")
