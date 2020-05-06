"""
Из файла names.txt в папке с фотками делает файл train.txt
То есть в него пишет только имена фоток .jpg игнорируя .txt

"""

with open(r"C:\CREESTL\Programming\PythonCoding\semestr_3\Yolo_mark-master\Yolo_mark-master\x64\Release\data\img\names.txt", "r") as f:
    lines = f.readlines()
    names = []
    for line in lines:
        if line[7:10] == "txt":
            pass
        elif line[7:10] == "jpg":
            names.append(r"/content/darknet/build/darknet/x64/data/obj/" + line)

with open(r"C:\CREESTL\Programming\PythonCoding\semestr_3\x64\data\train.txt", "w") as f:
    for name in names:
        f.write(name)
