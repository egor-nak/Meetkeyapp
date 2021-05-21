import os

with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/canstart.txt', 'w') as file:
    file.write('No')
os.system('python /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/mainapp.py & python /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/mainvideochange.py')