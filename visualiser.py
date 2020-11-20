import time 
import sys 
import os 
from AudioBar import AudioBar
import librosa
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
import pygame
import playsound

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'
HEIGHT = 12

def display(bar_heights):
    sys.stdout.write((HEIGHT) * CURSOR_UP_ONE + ERASE_LINE + "\r")

    for i in range(HEIGHT):
        line = ''
        for j in bar_heights:
            if j >= HEIGHT - i:
                line += '|'
            else:
                line += ' '
        sys.stdout.write('\n ' + line)
    sys.stdout.flush()

def main():
    # Some lines of the following have been shamelessly stolen from https://gitlab.com/avirzayev/medium-audio-visualizer-code/-/blob/master/main.py

    audio = "path/to/file.mp3"
    
    # Convert to wav
    sound = AudioSegment.from_mp3(audio)
    sound.export("path/to/file.wav", format="wav")
    
    filename = "path/to/file.wav"

    # getting information from the file
    time_series, sample_rate = librosa.load(filename)
    
    # getting a matrix which contains amplitude values according to frequency and time indexes
    stft = np.abs(librosa.stft(time_series, hop_length=512, n_fft=2048*4))

    # converting the matrix to decibel matrix
    spectrogram = librosa.amplitude_to_db(stft, ref=np.max)  

    # getting an array of frequencies
    frequencies = librosa.core.fft_frequencies(n_fft=2048*4)  

    # getting an array of time periodic
    times = librosa.core.frames_to_time(np.arange(spectrogram.shape[1]), sr=sample_rate, hop_length=512, n_fft=2048*4)

    time_index_ratio = len(times)/times[len(times) - 1]

    frequencies_index_ratio = len(frequencies)/frequencies[len(frequencies)-1]
    pygame.init()


    screen_w = 300
    screen_h = 250

    bars = []
    frequencies = np.arange(100, 8000, 100)
    r = len(frequencies)
    width = screen_w/r
    x = (screen_w - width*r)/2

    for c in frequencies:
        bars.append(AudioBar(x, 200, c, (255, 0, 0), max_height=250, width=width))
        x += width

    t = int(round(time.time() * 1000))
    start_time = t
    getTicksLastFrame = t

    # Use pygame to play the song. Trying to not use pygame though.
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(0)

    sys.stdout.write(2 * CURSOR_UP_ONE + ERASE_LINE)

    # How do you terminate this loop when the song ends? It's an infinite loop at the moment, can only be terminated with Ctrl + C
    while True:

        t = int(round(time.time() * 1000))
        deltaTime = (t - getTicksLastFrame) / 1000.0
        getTicksLastFrame = t
        
        # Store the heights of all the bars in a list
        bar_heights = []

        for b in bars:
            b.update(deltaTime, spectrogram[int(b.freq * frequencies_index_ratio)][int(((t - start_time)/1000.0) * time_index_ratio)])
            bar_heights.append(int(b.height / 10))
        
        # Display the bars
        display(bar_heights)

# Driver program 
if __name__ == '__main__':  
    main()
