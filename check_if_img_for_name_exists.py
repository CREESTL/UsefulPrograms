"""
Проверяет есть ли картинка для текстового файла
"""

with open(r"C:\CREESTL\Programming\PythonCoding\AlexeyABfork\darknet-master\build\darknet\x64\data\obj_reserve\names.txt") as names:
    lines = names.readlines()
    for line in lines:
        if line[0] == "n":
            continue
        try:
            open("C:\\CREESTL\\Programming\\PythonCoding\\AlexeyABfork\\darknet-master\\build\\darknet\\x64\\data\\obj\\" + str(line[:6]) + ".jpg")
        except:
            print("NO JPG FILE: " + "C:\\CREESTL\\Programming\\PythonCoding\\AlexeyABfork\\darknet-master\\build\\darknet\\x64\\data\\obj\\" + str(line[:6]) + ".jpg")