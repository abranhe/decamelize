mport unittest
import decamelize

class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(tocamelcase.convert("NonCamelCase"), "non_camel_case")

if __name__ == '__main__':
    unittest.main()
