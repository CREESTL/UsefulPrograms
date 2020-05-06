import os
"""
Переименовывает все картинки в папке к расширению .jpg
"""

def rename(folder_path):
    files = os.listdir(folder_path)
    for file in files:
        if file[-3:] != "txt":
            pos = file.find(".")
            new_file = file[:pos] + ".jpg"
            os.rename(folder_path + "\\" + file, folder_path + "\\" + new_file)
            print(new_file)
        if file[-4:] == "jpg~":
            os.remove(folder_path + "\\" + file)

rename(r"C:\CREESTL\Programming\PythonCoding\semestr_3\Yolo_mark-master\Yolo_mark-master\x64\Release\data\img")