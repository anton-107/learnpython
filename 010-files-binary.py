# coding=utf-8
from struct import pack


fw = open("data/data.bin", mode="wb")
buffer = pack("iii", 1, 2, 3)
fw.write(buffer)
fw.close()

nr1, nr2, nr3 = 0, 0, 0
fr = open("data/data.bin", mode="rb")
print(fr.read(3 * 4))
fr.close()
