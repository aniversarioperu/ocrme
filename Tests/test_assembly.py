import os
import unittest

from ocrme import assembly


class AssemblyTest(unittest.TestCase):

    def setUp(self):
        self.filename_base = "text_to_assembly"

    def test_assembly(self):
        assembly.assembly(self.filename_base)
        f = open(self.filename_base + ".txt", "r")
        result = f.readlines()
        f.close()

        expected_file_contents = ["1\n", "2\n", "3\n"]
        self.assertEqual(result, expected_file_contents)
        os.remove(self.filename_base + ".txt")


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)
