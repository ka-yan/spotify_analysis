### Spotify Listening History Analysis

This program visualizes the audio features of your top songs over time. You can use this program to analyze audio features of different playlists as well.

## How To Run

First, you'll need to get your spotify client id and client token from your spotify developer account and also get the list of your top 50 songs over time.

I suggest using favoritemusic.guru to get the lists of the songs. Then, you will need to get the lists of the songs in different .csv files naming them
```AllTimeTracks.csv``` 
```SixMonthTracks.csv```
```OneMonthTracks.csv```
```RecentTracks.csv```

This way, you should be able to run the program.

Libraries required:
1. spotipy
2. tkinter
3. matplotlib