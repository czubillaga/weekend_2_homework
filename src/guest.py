class Guest:

    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet

    def adjust_wallet(self, amount):
        self.wallet += amount