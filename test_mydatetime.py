import unittest


class MyDateTime(object):
    def __init__(self, year=2004, month=5, day=20):
        # isian year, month, dan day diberikan nilai tertentu sebagai tanda bahwa itu adalah opsional

        # untuk menyimpan nilai year, month, dan day agar bisa diakses dari class MyDateTime digunakan perintah self
        self.year = year
        self.month = month
        self.day = day

    def __add__(self, other):
        if isinstance(other, TimeDelta):
            return MyDateTime(day=self.day + other.days,
                              month=self.month + other.months,
                              year=self.year + other.years)


class TimeDelta(object):
    def __init__(self, days=0, months=0, years=0):
        self.days = days
        self.months = months
        self.years = years


class MyDateTimeTest(unittest.TestCase):
    def test_mydatetime(self):
        d = MyDateTime(year=2020, month=5, day=26)
        self.assertEqual(2020, d.year)
        self.assertEqual(5, d.month)
        self.assertEqual(26, d.day)

        # untuk menguji penjumlahan tanggal
        delta = TimeDelta(days=3)

        # rumus harus diurutkan sesuai dengan urutan pendefinisian variabel
        d2 = d + delta
        self.assertEqual(29, d2.day)
        self.assertEqual(5, d2.month)
        self.assertEqual(2020, d2.year)

        # jika ingin melakukan pengujian untuk penambahan tanggal, bulan, tahun
        delta = TimeDelta(days=3, months=2, years=1)

        d2 = d + delta
        self.assertEqual(29, d2.day)
        self.assertEqual(7, d2.month)
        self.assertEqual(2021, d2.year)
