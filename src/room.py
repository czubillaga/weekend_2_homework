class Room:

    def __init__(self, songs, guests, capacity):
        self.songs = songs
        self.guests = guests
        self.capacity = capacity

    def check_in(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)

    def check_out(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)