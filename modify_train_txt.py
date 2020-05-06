"""
Этот скрипт меняет пути к фоткам в файле на компе на пути на колабе
После этого данный файл (train.txt) надо залить на диск и скопировать в колаб
"""

def delete_last_line(path):
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
        f.close()
    with open(path, "w") as f:
        for line in lines:
            f.write(line)

def modify(path):
    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'
    with open(path, 'rb') as open_file:
        content = open_file.read()
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    with open(path, 'wb') as open_file:
        open_file.write(content)

"""
Всего 3572 фотки 
"""


with open(r"C:\CREESTL\Programming\PythonCoding\semestr_3\x64\data\train.txt", "w") as f:
    for i in range(1, 3573):
        line = "/content/darknet/build/darknet/x64/data/obj/{:06}.jpg".format(i)
        f.write(line + "\n")

f.close()

delete_last_line(r"C:\CREESTL\Programming\PythonCoding\semestr_3\x64\data\train.txt")
modify(r"C:\CREESTL\Programming\PythonCoding\semestr_3\x64\data\train.txt")
