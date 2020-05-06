'''
Указываешь путь - все фотки нумеруются с указанного номера до конца
'''

import os

'''
В конце пути НЕ ставить "\" после имени папки, в которой лежат фотки
'''
def rename(folder_path, start_number):
    files = os.listdir(folder_path)
    i = start_number + 1
    for file in files:
        print("Old name: ", file)
        new_file = "{:06}".format(i) + ".jpg"
        print("New name: ", new_file, "\n")
        os.rename(folder_path + "\\" + file, folder_path + "\\" + new_file)

        i += 1

folder_path = input("Введите путь к папке для переименования файлов в ней: ")
start_number = int(input("Введите номер последней фотографии в предыдущей папке: "))

rename(folder_path, start_number)