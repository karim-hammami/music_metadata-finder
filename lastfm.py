import os
import requests
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('LASTFM')
print("API_KEY: " + str(API_KEY))


print("Song Name: ")
reqSong = input()
raw = {"": reqSong}
half = urllib.parse.urlencode(raw)
song  = half[1:]
print(song)

print("Artist Name: ")
reqArtist = input()
rawart = {"": reqArtist}
halfart = urllib.parse.urlencode(rawart)
arti = halfart[1:]
print(arti)


format = "format=json"
BASE_URL = "http://ws.audioscrobbler.com/2.0"
URL = BASE_URL+"/?method=track.getInfo&api_key="+str(API_KEY)+"&artist="+arti+"&track="+song+"&"+format

r = requests.get(URL)
data = r.json()

trackName = data["track"]["name"]
artistName = data["track"]["artist"]["name"]
try: 
    albumName = data["track"]["album"]["title"]
except:
    albumName = "not found"
try:
    genre = data["track"]["toptags"]["tag"][0]["name"]
except:
    genre = "not found"

print("Track Name: "+trackName)
print("Artist Name: "+artistName)
print("Album Name: "+albumName)
print("Genre: "+genre)


