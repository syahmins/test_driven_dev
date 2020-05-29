import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add(self):
        c = Calculator()
        hasil = c.add(2, 6)
        # untuk yang di dalam kurung, (hasil yang seharusnya, return dari rumus)
        # cek dengan menekan tombol run
        self.assertEqual(8, hasil)

    def test_substract(self):
        c = Calculator()
        hasil = c.sub(3, 2)
        # untuk yang di dalam kurung, (hasil yang seharusnya, return dari rumus)
        # cek dengan menekan tombol run
        self.assertEqual(1, hasil)
