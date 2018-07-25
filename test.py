import unittest
import decamelize

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(decamelize.convert("CamelCase"), "camel_case")

if __name__ == '__main__':
    unittest.main()
