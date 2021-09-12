class Room:

    def __init__(self, songs, guests, capacity):
        self.songs = songs
        self.guests = guests
        self.capacity = capacity
        self.entry_fee = 5

    def check_in(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
            guest.adjust_wallet(-self.entry_fee)

    def check_out(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)