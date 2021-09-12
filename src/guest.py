class Guest:

    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet

    def adjust_wallet(self, amount):
        self.wallet += amount

    def cheer_for_song(self, room):
        if self.favourite_song in room.songs:
            return "Whoo!"

    def buy(self, bar, item):
        bar.sell(self.name, item)