import glob
import subprocess


def do_ocr():
    for i in glob.glob("*pdf"):
        filename_base = i.replace(".pdf", "")
        cmd = "pdftoppm " + i + " " + filename_base
        print(cmd)
        #p = subprocess.check_call(cmd, shell=True)

        for j in glob.glob(filename_base + "-*"):
            new_filename_base = j.replace(".ppm", "")
            print(new_filename_base)
            cmd = "tesseract " + j + " " + new_filename_base + " -l spa"
            print(cmd)
        #p = subprocess.check_call(cmd, shell=True)
    # pdftoppm Resolucion_000099-2013-1390770268066.pdf a

def assembly(filename_base):
    print("hola")


if __name__ == "__main__":
    main()
