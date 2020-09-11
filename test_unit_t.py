import t
import unittest

class Test_TestIncr(unittest.TestCase):
    def test_incr(self):
        self.assertEqual(t.incr(3), 4)

    def test_decr(self):
        self.assertEqual(t.decr(4), 3)

if __name__ == '__main__':
    unittest.main()