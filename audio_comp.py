import audio_wav

op_code = {"C4": 262, "C#4": 277, "D4": 294, "D#4": 311,
           "E4": 330, "F4": 349, "F#4": 370, "G4": 392,
           "G#4": 415, "A4": 440, "A#4": 466, "B4": 494,
           "C5": 523, "C#5": 554, "D5": 587, "D#5": 622,
           "E5": 659, "F5": 698, "F#5": 740, "G5": 784,
           "G#5": 831, "A5": 880, "A#5": 932, "B5": 988}

samples = 0

def read(entrada):
    global samples
    test = open(entrada, "r")
    word = ""
    words = []
    for line in test:
        line = line + " "
        for letter in line:
            if letter == "*":
                break
            elif letter != " " and letter != "\n" and letter != "\t":
                word = word + letter
            else:
                if word != "":
                    words.append(word)
                word = ""

    audio = []
    for i in range(len(words)):
        if words[i].upper() == "X":
            f1 = op_code[words[i + 1].upper()]
            a1 = int(words[i + 2])
            f2 = op_code[words[i + 3].upper()]
            a2 = int(words[i + 4])
            smp = int(words[i + 5])
            samples += smp
            audio.append(audio_wav.Audio.append(smp, (f1, a1), (f2, a2)))
    return audio

class Compile:
    @staticmethod
    def audio(entrada, salida):
        global samples
        output = open(salida, "bw")
        audio = read(entrada)
        header = audio_wav.Audio.header(samples)

        wave = []
        for array in header:
            for element in array:
                wave.append(element)

        for array in audio:
            for element in array:
                wave.append(element)

        output.write(bytearray(wave))