import unittest
from make_image import make_image


class TestMakeImage(unittest.TestCase):

    def test_type(self):
        self.assertEqual(type(make_image("test", 1, as_array=True)).__name__, "ndarray")

    def test_shape(self):
        self.assertEqual(make_image("test", 1, as_array=True).shape, (16, 150))


if __name__ == '__main__':
    unittest.main()
