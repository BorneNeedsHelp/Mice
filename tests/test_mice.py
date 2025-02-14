import unittest
from Mice import Mice
class TestMice(unittest.TestCase):
    def test_create_cookie(self):
        self.assertEqual(Mice.Mice.create_cookie('jdf', 100, 'test.com', '/', True, False, 'Lax', lang='en'), 0)
        self.assertEqual(Mice.Mice.create_cookie('shfjd', 273548320, 'test.com', '/', False, False, 'Lax', lang='en', pref='dark', pref2='bold', textsize=16), 1)

    def test_encode_cookie(self):
        self.assertEqual(Mice.Mice.encode_cookie_data("Set-Cookie: user_id=jdf; Path=/; Expires=Fri, 14 Feb 2025 03:54:12 GMT; Max-Age=100; Domain=test.com; HttpOnly; SameSite=Lax; lang=en"), 2)
        self.assertEqual(Mice.Mice.encode_cookie_data("Set-Cookie: user_id=isnotherelol!; Path=/; Expires=Fri, 14 Feb 2025 03:54:12 GMT; Max-Age=100; Domain=test.com; SameSite=Lax; lang=sp"), 3)

    def test_decode_cookie(self):
        self.assertEqual(Mice.Mice.decode_cookie_data("IlNldC1Db29raWU6IHVzZXJfaWQ9amRmOyBQYXRoPS87IEV4cGlyZXM9RnJpLCAxNCBGZWIgMjAyNSAwMzo1NDoxMiBHTVQ7IE1heC1BZ2U9MTAwOyBEb21haW49dGVzdC5jb207IEh0dHBPbmx5OyBTYW1lU2l0ZT1MYXg7IGxhbmc9ZW4i"), 4)
