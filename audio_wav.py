import math

def integer(n, size):
    result = []
    a = 255
    for i in range(0, size, 1):
        b = (n & a) >> (8 * i)
        result.append(b)
        a = a << 8
    return result

def string(line):
    result = []
    for letter in line:
        result.append(ord(letter))
    return result

class Audio:
    @staticmethod
    def header(samples):
        temp = []
        temp.append(string("RIFF"))
        temp.append(integer(samples + 44, 4))
        temp.append(string("WAVE"))
        temp.append(string("fmt "))
        temp.append(integer(16, 4))
        temp.append(integer(1, 2))
        temp.append(integer(1, 2))
        temp.append(integer(8000, 4))
        temp.append(integer(8000, 4))
        temp.append(integer(1, 2))
        temp.append(integer(8, 2))
        temp.append(string("data"))
        temp.append(integer(samples, 4))
        return temp

    @staticmethod
    def append(samples, ch1, ch2):
        temporal = []
        for i in range(samples):
            f1 = ch1[1] * math.sin(2 * math.pi * ch1[0] * i / 8000)
            f2 = ch2[1] * math.sin(2 * math.pi * ch2[0] * i / 8000)
            temporal.append(int(127 - (f1 + f2)))
        return temporal