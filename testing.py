import speech_recognition as sr
import os


def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


def record_volume(indx):
    r = sr.Recognizer()
    prev = ''
    while True:
        with open('stopall.txt',
                  'r') as file:
            if file.read() == 'Yes':
                quit()
        with open("canfindcheckword.txt",
                  'r') as file:
            ans = file.read()
        if ans == 'Yes':
            if prev != 'Yes':
                os.system("SwitchAudioSource -s MEETKEY")
            try:
                with sr.Microphone(device_index=indx) as source:
                    print('listen')
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                try:
                    query = r.recognize_google(audio, language='ru-RU')
                    print(query)
                    with open("checkword.txt", "r") as file:
                        cont = file.read()
                    if cont.lower() in query.lower() and cont != 'Nothing223':
                        notify("MEETKEY", 'Checkword', f'someone say {cont}')
                except Exception:
                    print('')
            except Exception:
                print('Nothing')
        else:
            if prev != 'No':
                os.system("SwitchAudioSource -s 'Built-in Output'")
        prev = ans


os.system("SwitchAudioSource -s 'Built-in Output'")
indx = sr.Microphone.list_microphone_names().index('MEETKEY')
print(sr.Microphone.list_microphone_names()[indx])
try:
    record_volume(indx)
except KeyboardInterrupt:
    os.system("SwitchAudioSource -s 'Built-in Output'")