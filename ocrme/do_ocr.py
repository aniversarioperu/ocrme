import glob
import subprocess


def do_ocr(pdf_file):
    filename_base = pdf_file.replace(".pdf", "")
    cmd = "pdftoppm " + pdf_file + " " + filename_base
    print(cmd)
    p = subprocess.check_call(cmd, shell=True)

    for j in glob.glob(filename_base + "-*ppm"):
        new_filename_base = j.replace(".ppm", "")
        print(new_filename_base)
        cmd = "tesseract " + j + " " + new_filename_base + " -l spa"
        print(cmd)
        p = subprocess.check_call(cmd, shell=True)
    if p == 0:
        return filename_base


if __name__ == "__main__":
    main()
