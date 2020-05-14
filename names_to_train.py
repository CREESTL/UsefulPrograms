"""
Из файла names.txt в папке с фотками делает файл train.txt
То есть в него пишет только имена фоток .jpg игнорируя .txt

"""
path = input("Введите путь к файлу names.txt, чтобы преобразовать его в train.txt: \n")

with open(path + "/names.txt", "r") as f:
    lines = f.readlines()
    names = []
    for line in lines:
        if line[7:10] == "txt":
            pass
        elif line[7:10] == "jpg":
            names.append(r"data/obj/" + line)

with open(path + "/train.txt", "w") as f:
    for name in names:
        f.write(name)
