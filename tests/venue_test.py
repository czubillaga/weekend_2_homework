import unittest

from src.song import Song
from src.guest import Guest
from src.room import Room
from src.venue import Venue

class TestVenue(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Frank Ocean", "Godspeed")
        self.song2 = Song("Kodak Black", "Tunnel Vision")
        self.guest1 = Guest("Carlos Zubillaga", self.song1)
        self.guest2 = Guest("Oscar Webber", self.song2 )
        self.room1 = Room([self.song1], [self.guest1])
        self.room2 = Room([self.song2], [self.guest2])
        self.venue = Venue("Karaoke Bar", [self.room1, self.room2], 1000)

    def test_venue_properties(self):
        self.assertEqual("Karaoke Bar", self.venue.name)
        self.assertEqual(1000, self.venue.till)
        self.assertEqual("Carlos Zubillaga", self.venue.rooms[0].guests[0].name)
        self.assertEqual("Godspeed", self.venue.rooms[0].songs[0].title)