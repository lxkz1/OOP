class Playlist:
    def __init__(self, name):
        self.name = name
        self.playlists = []

    def add_song(self,song):
        if song in self.playlists:
            print("Song Already in playlists")
        else:
            self.playlists.append(song)
            print(f"{song.title} successfully added to the {self.name} playlists")

    def remove_song(self,song):
        if song not in self.playlists:
            print("Song is not in the playlists and cannot be removed")
        else:
            self.playlists.remove(song)
            print(f"{song.title} successfully removed from the {self.name} playlists")

    def show_song(self):
         for song in self.playlists:
            print(f"{song.title} by {song.artist} with a duration of {song.length} seconds")

    def total_minutes_and_seconds(self):
        total_sec = 0
        for song in self.playlists:
            time_per_song = int(song.length)
            total_sec += time_per_song
        minutes = total_sec // 60
        seconds = total_sec % 60
        if seconds != 0:
            print(f"The playlist lastes {minutes} minutes and {seconds}")
        else:
            print(f"The playlist lastes {minutes} minutes")



class Song:
    def __init__(self,title,artist,length):
        self.title = title
        self.artist = artist
        self.length = length

    def describe(self):
        print(f"{self.title} by {self.artist} that last's {self.length} second's")


song1 = Song("Bohemian Rhapsody", "Queen", 354)
song2 = Song("Blinding Lights", "The Weeknd", 200)
song3 = Song("Hotel California", "Eagles", 391)
song4 = Song("Imagine", "John Lennon", 183)
song1.describe()
song2.describe()
playlist = Playlist("Road Trip")
playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)
playlist.add_song(song1)
playlist.remove_song(song2)
playlist.remove_song(song4)
print("Songs in playlist:", len(playlist.playlists))
playlist.show_song()
playlist.total_minutes_and_seconds()
