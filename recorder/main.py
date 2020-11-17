# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import os


# Sampling frequency
freq = 48000

# Recording duration
duration = 2

count = 0

def record(filename):
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    save(recording, filename, freq)

def save(recording, filename, freq):
	global count
	os.makedirs("./data/"+filename, exist_ok=True)
	write("./data/" + filename + "/" + filename + "_" + str(count)+".wav" , freq, recording)



if __name__ == "__main__":
    while(True):
        count = 0
        cmd = "n"
        inp = str(input("Word: "))
        print("#" * 20)
        while(cmd == "n"):
            if(cmd == "n"):
                record(inp)
                count += 1
            elif(cmd == "w"):
                count = 0
                continue

            cmd = str(input("Command: "))

        