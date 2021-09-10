class Room:

    def __init__(self, songs, guests):
        self.songs = songs
        self.guests = guests

    def check_in(self, guest):
        self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)