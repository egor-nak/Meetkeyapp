import os

with open('canstart.txt', 'w') as file:
    file.write('No')
with open('path.txt', 'w') as file:
    file.write('Nothing')
with open('checkword.txt', 'w') as file:
    file.write('Nothing223')
with open("filtername.txt", 'w') as pat:
    pat.write('Nothing223')
with open("canfindcheckword.txt", 'w') as pat:
    pat.write('No')
with open("stopall.txt", 'w') as pat:
    pat.write('No')
print('Stop')
os.system('python mainapp.py & python mainvideochange.py & python testing.py')
