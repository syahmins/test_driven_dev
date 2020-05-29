import unittest
import datetime


class CobaDateTime(unittest.TestCase):
    def test_datetime(self):
        d = datetime.date(year=2020, month=5, day=26)

        # efeknya sama
        self.assertTrue(d.year == 2020)
        self.assertEqual(2020, d.year)
        self.assertEqual(d.year, 2020)

        # untuk mengecek hitungan beberapa waktu ke depan
        # contoh untuk mengecek apakah tiga hari ke depan adalah tanggal 29
        delta = datetime.timedelta(days=3)
        d2 = delta + d
        self.assertEqual(29, d2.day)
