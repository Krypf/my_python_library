# tests/test_my_module.py

import unittest
from my_python_library import my_module

class TestMyModule(unittest.TestCase):
    def test_my_function(self):
        self.assertEqual(my_module.my_function(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
