import unittest

anums = [1000, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
rnums = "M D CD C XC L XL X IX V IV I".split()


def to_roman(x):
    ret = []
    for a, r in zip(anums, rnums):
        n, x = divmod(x, a)
        ret.append(r * n)
    return ''.join(ret)


class ToRoman(unittest.TestCase):

    def test_m(self):
        self.assertEqual(to_roman(1000), 'M')

    def test_d(self):
        self.assertEqual(to_roman(500), 'D')

    def test_cd(self):
        self.assertEqual(to_roman(400), 'CD')

    def test_c(self):
        self.assertEqual(to_roman(100), 'C')

    def test_xc(self):
        self.assertEqual(to_roman(90), 'XC')

    def test_l(self):
        self.assertEqual(to_roman(50), 'L')

    def test_xl(self):
        self.assertEqual(to_roman(40), 'XL')

    def test_x(self):
        self.assertEqual(to_roman(10), 'X')

    def test_ix(self):
        self.assertEqual(to_roman(9), 'IX')

    def test_v(self):
        self.assertEqual(to_roman(5), 'V')

    def test_iv(self):
        self.assertEqual(to_roman(4), 'IV')

    def test_i(self):
        self.assertEqual(to_roman(1), 'I')


if __name__ == '__main__':
    unittest.main()
