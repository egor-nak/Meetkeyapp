import pyaudio
import wave
import os
import speech_recognition as sr


def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


word = 'Егор'
r = sr.Recognizer()
last = ''
alltext = []
while True:
    try:
        filename = "output.wav"
        with sr.AudioFile(filename) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            try:
                text = r.recognize_google(audio_data, language="ru-RU")
                if last != text:
                    print(text)
                    alltext.append(text)
                    if word in text:
                        notify(title='MEETKEY',
                               subtitle='В конференции возможно прозвучало контрольное слово',
                               message=alltext[-1] + ' ' + text)

                last = text
            except Exception:
                print('Нифига ничего не понятно даже мне')
    except Exception:
        pass
