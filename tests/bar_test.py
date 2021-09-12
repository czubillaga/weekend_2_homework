import unittest
from src.guest import Guest
from src.song import Song
from src.bar import Bar

class TestBar(unittest.TestCase):

    def setUp(self):
        self.song = Song("Frank Ocean", "Godspeed")
        self.guest = Guest("Carlos Zubillaga", self.song, 30)
        self.bar = Bar(1000)

    def test_start_tab(self):
        self.bar.start_tab(self.guest)
        self.assertEqual("Carlos Zubillaga", self.bar.guests[0]["object"].name)
        self.assertEqual(0, self.bar.guests[0]["tab"])

    def test_get_tab(self):
        self.bar.start_tab(self.guest)
        self.assertEqual(0, self.bar.get_tab(self.guest))

    def test_sell(self):
        self.bar.start_tab(self.guest)
        self.guest.buy(self.bar, "Tennents")
        self.assertEqual(3.60, self.bar.guests[0]["tab"])
        self.assertEqual(["Tennents"], self.bar.guests[0]["items_purchased"])

    def test_close_tab(self):
        self.bar.start_tab(self.guest)
        self.guest.buy(self.bar, "Tennents")
        self.bar.close_tab(self.guest)
        self.assertEqual(0, len(self.bar.guests))
        self.assertEqual(1003.6, self.bar.till)
        self.assertEqual(26.4, self.guest.wallet)