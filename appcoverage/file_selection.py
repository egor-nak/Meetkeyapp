import easygui

with open("path.txt", 'w') as file:
    file.write('Nothing')
path = easygui.fileopenbox()
try:
    print(len(path))
    with open("path.txt", 'w') as file:
        file.write(path)
except Exception:
    with open("path.txt", 'w') as file:
        file.write("Nothing2")
