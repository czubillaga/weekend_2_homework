import unittest

from src.song import Song
from src.guest import Guest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Frank Ocean", "Godspeed")
        self.song2 = Song("Kodak Black", "Tunnel Vision")
        self.guest1 = Guest("Carlos Zubillaga", self.song1)
        self.guest2 = Guest("Oscar Webber", self.song2 )
        self.room = Room([], [])

    def test_check_in_guests(self):
        self.room.check_in(self.guest1)
        self.assertEqual("Carlos Zubillaga", self.room.guests[0].name)

    def test_check_out_guests(self):
        self.room.check_in(self.guest1)
        self.room.check_in(self.guest2)
        self.room.check_out(self.guest1)
        self.assertEqual("Oscar Webber", self.room.guests[0].name)

    def test_add_songs_to_room(self):
        self.room.add_song(self.song1)
        self.assertEqual("Godspeed", self.room.songs[0].title)
        