import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Frank Ocean", "Godspeed")

    def test_song_has_title(self):
        self.assertEqual("Godspeed", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Frank Ocean", self.song.artist)
