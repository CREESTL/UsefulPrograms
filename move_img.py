"""
Скрипт по перемещению (не копированию) всех картинок разных типов из разных папок в одну для лейблинга
Фактически мы просто берем путь к загруженной фотке и в нем меняем
название родной папки на ту, в которую мы хоти переместить
Тем самым картинки удаляются из старой папки
"""
import os
from shutil import copy

folders = ["dumps", "long_trucks", "fork_lifters", "heavy_loaders", "excavators"]
path = r"C:\CREESTL\Programming\PythonCoding\Hackathon(custom counter)"

i = 0
for folder in folders:
    for image in os.scandir(folder): #итерация для каждой картинки
        i += 1 #счетчик
        #Это удалит файлы из начальных директорий, так что не используем
        #os.rename(image.path, os.path.join(path, "{:06}.jpg".format(i))) #создаем путь сохранения ля каждой нумерованной картинки (до 6 цифр)
        copy(image.path, os.path.join(path, "{:06}.jpg".format(i)))