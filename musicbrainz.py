import requests
import urllib.parse

# get the song name and encode it properly

print("Song Name: ")
reqSong = input()
raw = {"": reqSong}
half = urllib.parse.urlencode(raw)
song  = half[1:]
print(song)

# get the artist name and encode it properly

print("Artist Name: ")
reqArtist = input()
rawart = {"": reqArtist}
halfart = urllib.parse.urlencode(rawart)
arti = halfart[1:]
print(arti)

# concat the musicbrainz API with the inputs

URL = "https://musicbrainz.org/ws/2/recording/?query=recording:"+song+"%20artist:"+arti+"&fmt=json&inc="
print(URL)

# make the GET request to the API

r = requests.get(URL)
data = r.json()

# select the wanted data and handle the exception when the API can't return data for genre

artist = data["recordings"][0]["artist-credit"][0]["name"]
trackName = data["recordings"][0]["title"]
album = data["recordings"][0]["releases"][0]["title"]
try:
    genre = data["recordings"][0]["tags"][0]["name"]
except KeyError:
    genre = "Could not find Genre"
year = data["recordings"][0]["first-release-date"]

# print the results

print("Artist: "+artist)
print("Track: "+trackName)
print("Album: "+album)
print("Genre: "+genre)
print("Year: "+year)
