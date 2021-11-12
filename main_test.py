import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_sum_to_6(self):
        self.assertEqual(main.sum_to(6), 21)

    def test_sum_to_10(self):
        self.assertEqual(main.sum_to(10), 55)

    def test_largest_1(self):
        self.assertEqual(main.largest([1, 2, 3, 4, 0]), 4)

    def test_largest_2(self):
        self.assertEqual(main.largest([10, 4, 2, 231, 91, 54]), 231)

    def test_occurrences_1(self):
        self.assertEqual(main.occurrences('fleep floop', 'e'), 2)

    def test_occurrences_2(self):
        self.assertEqual(main.occurrences('fleep floop', 'p'), 2)

    def test_occurrences_3(self):
        self.assertEqual(main.occurrences('fleep floop', 'ee'), 1)

    def test_occurrences_4(self):
        self.assertEqual(main.occurrences('fleep floop', 'fe'), 0)

    def test_product_1(self):
        self.assertEqual(main.product(-1, 4), -4)

    def test_product_2(self):
        self.assertEqual(main.product(2, 5, 5), 50)

    def test_product_3(self):
        self.assertEqual(main.product(4, 0.5, 5), 10)

if __name__ == '__main__':
    unittest.main()
