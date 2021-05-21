# you sould start this comand in terminal to install some stuff for this function
# put this into terminal "sudo gem install terminal-notifier"
import os
import time


# The notifier function
def notify(title, subtitle, message):
    t = '-title {!r}'.format(title)
    s = '-subtitle {!r}'.format(subtitle)
    m = '-message {!r}'.format(message)
    os.system('terminal-notifier {}'.format(' '.join([m, t, s])))


time.sleep(12)
# Calling the function
notify(title='MEETKEY',
       subtitle='',
       message='В конференции возможно прозвучало контрольное слово')


