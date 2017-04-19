#Use youtube-dl or pytube to grab playlist?
#This will find song information based off file name.
import spotipy
import sys
import pprint

search_str = 'Deathcab'

sp = spotipy.Spotify()
result = sp.search(search_str)
pprint.pprint(result)