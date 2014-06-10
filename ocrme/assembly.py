# -*- coding: utf-8 -*-
import codecs
import glob


def assembly(filename_base):
    files = []
    for i in glob.glob(filename_base + "-*txt"):
        files.append(i)
    files.sort()

    out = ""
    for i in files:
        f = codecs.open(i, "r", "utf-8")
        out += f.read()
        f.close()

    with codecs.open(filename_base + ".txt", "w", "utf-8") as writer:
        writer.write(out)


if __name__ == "__main__":
    assembly("test")
