import unittest

from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.favourite_song = Song("Frank Ocean", "Godspeed")
        self.guest = Guest("Carlos Zubillaga", self.favourite_song)

    def test_guest_has_name(self):
        self.assertEqual("Carlos Zubillaga", self.guest.name)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Godspeed", self.favourite_song.title)
        self.assertEqual("Frank Ocean", self.favourite_song.artist)