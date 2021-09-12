import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.favourite_song = Song("Frank Ocean", "Godspeed")
        self.guest = Guest("Carlos Zubillaga", self.favourite_song, 10)

    def test_guest_has_name(self):
        self.assertEqual("Carlos Zubillaga", self.guest.name)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Godspeed", self.favourite_song.title)
        self.assertEqual("Frank Ocean", self.favourite_song.artist)

    def test_guest_wallet(self):
        self.guest.adjust_wallet(-5)
        self.assertEqual(5, self.guest.wallet)

    def test_guest_will_cheer(self):
        room = Room([self.favourite_song], [self.guest], 5)
        self.assertEqual("Whoo!", self.guest.cheer_for_song(room))