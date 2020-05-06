"""
Этот файл добавляет необходимые папки в начало каждой строки в файле train.txt для
того, чтобы путь к фотографиям был прописан верно
"""


def modify():
    path = input("Введите путь к файлу train.txt:\n")
    with open(path, 'r') as f:
        lines_from_file = f.readlines()
    lines = lines_from_file
    with open(path, 'w') as f:
        for line in lines:
            f.write("data/obj/"+ line)

modify()

