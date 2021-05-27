import os

with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/canstart.txt', 'w') as file:
    file.write('No')
with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/path.txt', 'w') as file:
    file.write('Nothing')
with open('/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/checkword.txt', 'w') as file:
    file.write('Nothing223')
with open("/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/filtername.txt", 'w') as pat:
    pat.write('Nothing223')
with open("/Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/canfindcheckword.txt", 'w') as pat:
    pat.write('No')
os.system('python /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/appcoverage/mainapp.py & python /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/mainvideochange.py & python /Users/egor.nakonechnyyicloud.com/PycharmProjects/MEETKEYmain/main/testing.py')