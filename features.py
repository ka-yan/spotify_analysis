"""
Name: Kalyan Khatiwada
Project 10
CS152 B
Date:2022/12/12

This python file gets the features of songs in a given filename and also plots the features with the help of matplotlib. This file is used in the main.py in which GUI is
used to choose the filename and which features to plot and analyze.

This file can be used in other files by:
for eg:
    features.getfeatures(Ids, feature)

where Ids is the track id of the songs and features are the audio features as given by Spotify API.


"""
#import statements
import spotipy
import stats
import matplotlib.pyplot as plt


#To get access to Spotify API
username = 'Kalyan Khatiwada'
client_id ='c80c79b993e74c218020d513e7b95551'
client_secret = '7e3071c4995548d795229c605711145b'
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-recently-played'

token = spotipy.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=client_id,   
                                   client_secret=client_secret,     
                                   redirect_uri=redirect_uri)


def get_tracks(filename):
    """This function gets the tracks from a file and returns them"""
    fp = open(filename, "r")
    line = fp.readline()
    songs=[]
    for lines in fp:
        items = lines.split(",")
        songs.append(items[0])
    return songs

def get_artists(filename):
    """This function gets the artists of the songs from a file and returns them"""
    fp = open(filename, "r")
    line = fp.readline()
    artists =[]
    for lines in fp:
        items = lines.split(",")
        artists.append(items[1])
    return artists

def get_id(filename):
    """This function uses get_tracks to get the track names and get_artists to get artists to get the track ids and returns them."""
    sp = spotipy.Spotify(auth = token)
    artists = get_artists(filename)
    songs = get_tracks(filename)
    trackId = []
    counter = 0
    while counter < len(artists):
        track_id = sp.search(q='artist:' + artists[counter] + ' track:' + songs[counter], type='track')
        trackId.append(track_id['tracks']['items'][0]['id'])
        counter +=1
    return trackId

def export(filename, newfilename):
    """This function exports the track songs, their artists and the ids."""
    artists = get_artists(filename)
    songs = get_tracks(filename)
    trackId = get_id(filename)
    file_out = open(newfilename, "w")
    file_out.close()
    file_output = open(newfilename, "a")
    file_output.write("Tracks" + "," + "Artists" + "," + "TrackId" +"\n")
    counter = 0
    while counter < len(artists):
        file_output.write(songs[counter] + "," + artists[counter] + "," + trackId[counter] + "\n")
        counter +=1
    file_output.close()

def getfeature(Ids, feature):
    """This function gets the specific feature that you want from a list of features and returns them"""
    sp = spotipy.Spotify(auth = token)
    TrackIds = Ids
    feature_list = []
    for id in TrackIds:
        features = sp.audio_features(id)
        feature_list.append(features[0][feature])
    return feature_list

def get_mean(filename, feature):
    """This function gets the mean of the feature that you choose and returns it."""
    Ids = get_id(filename)
    feature_list = getfeature(Ids, feature)
    mean_feature = stats.mean(feature_list)
    return mean_feature

def compare_mean(feature):
    """This function compares the mean of the features"""
    AllTimeMean = get_mean("AllTimeTracks.csv", feature)
    OneMonthMean = get_mean("OneMonthTracks.csv", feature)
    RecentMean = get_mean("RecentTracks.csv", feature)
    SixMonthMean = get_mean("SixMonthTracks.csv", feature)
    list_mean = [AllTimeMean, SixMonthMean, OneMonthMean, RecentMean]
    return list_mean

def plot_mean(feature):
    """This function plots the mean of the features over time."""
    list_mean = compare_mean(feature)
    list_data = ["All Time Tracks", "Six Month Tracks", "One Month Tracks", "Recent Tracks"]
    for x in range(len(list_mean)):
        plt.plot(list_data[x], list_mean[x], "-o")
    plt.title("Mean " + feature + " of Spotify Listening History")
    plt.xlabel("Most Listened")
    plt.ylabel("Mean " + feature + " of 50 songs")
    plt.show()

def plot_features(filename, feature):
    """This function plots the features of 50 songs according to the ranking of them."""
    Ids = get_id(filename)
    feature_list = getfeature(Ids, feature)
    track_rank = range(1,51)
    for x in range(len(feature_list)):
        plt.plot(track_rank[x], feature_list[x], "-o")
    plt.title("Mean " + feature + " of Spotify Listening History")
    plt.xlabel("Ranking of the song")
    plt.ylabel(feature + " of the songs")
    plt.show()