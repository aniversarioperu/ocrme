import os
import unittest

from ocrme import do_ocr


class AssemblyOCR(unittest.TestCase):

    def setUp(self):
        self.pdf_file = "text_to_ocr.pdf"
        self.filename_base = ""

    def test_ocr(self):
        p = do_ocr.do_ocr(self.pdf_file)
        self.filename_base = self.pdf_file.replace(".pdf", "")
        self.assertEqual(p, self.filename_base)

        result = os.path.isfile(self.filename_base + "-5.txt")
        self.assertEqual(result, True)
        os.remove(self.filename_base + "-1.txt")
        os.remove(self.filename_base + "-2.txt")
        os.remove(self.filename_base + "-3.txt")
        os.remove(self.filename_base + "-4.txt")
        os.remove(self.filename_base + "-5.txt")
        os.remove(self.filename_base + "-1.ppm")
        os.remove(self.filename_base + "-2.ppm")
        os.remove(self.filename_base + "-3.ppm")
        os.remove(self.filename_base + "-4.ppm")
        os.remove(self.filename_base + "-5.ppm")


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity = 2)
    unittest.main(testRunner=runner)
