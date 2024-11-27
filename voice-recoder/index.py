
# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import time


def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1
    print("Time's up!")


freq = 44100
duration = 5

# Start recorder with the given values 
# of duration and sample frequency
recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=1)

print("Recording Audio...")
countdown(duration)
sd.wait()
print("Audio recording completed!")

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)

# Convert the NumPy array to audio file
# wv.write("recording1.wav", recording, freq, sampwidth=2)
