"""PyAudio example: Record a few seconds of audio and save to a WAVE file."""

import os
import pyaudio
import wave
import speech_recognition as sr

os.system("SwitchAudioSource -s 'MEETKEY'")
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"
r = sr.Recognizer()
p = pyaudio.PyAudio()
# print(10)
indx = ''
for i in range(p.get_device_count()):
    if p.get_device_info_by_index(i)['name'] == 'MEETKEY':
        indx = p.get_device_info_by_index(i)['index']
    # print(p.get_device_info_by_index(i))
while True:
    # print("* recording")
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    input_device_index=3)
    print(10)
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    # print("* done recording")

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
