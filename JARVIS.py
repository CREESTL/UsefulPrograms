"""
Для тренировки YOLOv3 необходима папка obj, содержащая следующее
1) Файл 000001.jpg (изображение)
2) Файл 000001.txt (файл с текстовыми данными координат размеченного бокса на фото)

Зачастую возникают проблемы с созданием этой папки, которые сложно заметить, но они прерывают
процесс тренировки, что очесь сильно раздражает.
Поэтому я создал эту программу, которая устраняет все (наверное) проблемы за вас!

"""
import os
import time
from shutil import copyfile, copy

def get_path():
    print("Добрый день, мистер Старк!")
    while True:
        path = input("Пожалуйста, введите путь к папке с размеченными фотографиями: \n")
        if os.path.exists(path):
            return path
        else:
            print("Похоже вы указали путь не верно! Не могу найти такую папку ;(")

def wow():
    print("ПИУ! ПИУ! ПИУ! ПИУ! СДОХНИ ТАНООООООС!")
    time.sleep(5)

# Функция меняет расширение всех изображений на .jpg
def rename_to_jpg(path):
    invalid_files = []# список файлов, который стоит удалить
    for file in os.listdir(path):
        if (file[-4:] == ".png") or (file[-4:] == ".gif"):
            if file[:-4] + ".jpg" in os.listdir(path): # если нашли, например, 144.png но уже есть 144.jpg, то удаляем первый
                invalid_files.append(file)
            else:
                os.rename(path+ "/" + file, path + "/" + file[:-4] + ".jpg")
    return invalid_files # далее этот массив используется во всех других функциях


# функция проверяет, существует ли для каждого .jpg файла .txt файл и не пуст ли этот .txt файл
def check_if_txt_exists(path, invalid_files):
    i = 0
    print("Тааааакс...")
    time.sleep(1)
    for file in os.listdir(path):
        if (file[-4:] == ".jpg") and (i % 2 == 0):  # если позиция файла четная (счет с НУЛЯ) и он - фотка, то проверяем наличие соответствующего текстового файла
            if file[:6]+".txt" not in os.listdir(path):  # если для картинки нет текстового файла - онаа не была размечена
                print("Изображение {} не было размечено!".format(file))
                invalid_files.append(file)
                i += 1
            else:
                txt = file[:6]+".txt" # если для картинки есть текстовый файл, то проверяем его на пустоту
                with open(path + "/" + txt, "r") as f:
                    lines = f.readlines()
                    if lines != []:
                        pass
                    else:
                        invalid_files.append(file)  # если текстовый файл пуст, то удаляется И он, И картинка
                        invalid_files.append(txt)
                        print(txt + " пуст!")
                i += 1
        elif (file[-4:] == ".txt") and (i % 2 == 0):  # если позиция четная (счет с НУЛЯ), а на ней текстовый файл - его следует удалить
            print("Файл " + file + " не на своём месте!")
            invalid_files.append(file)
            i += 2 # здесь перескакиваем через один файл для правильности работы
        elif (file[-4:] == ".txt") and (i % 2 != 0):  # если позиция НЕчетная (счет с НУЛЯ), то текстовый файл на своем месте
            i += 1
    return invalid_files


# функция удаляет все файлы, которые не были размечены (у которых пустые .txt файлы)
def delete_invalid_files(invalid_files, path):
    if invalid_files != []:
        time.sleep(2)
        print("\n\nВот все некорректные файлы, которые я смог найти, Тони:\n")
        for file in invalid_files:
            print(file)
        choice = str(input("\nХотите ли вы удалить эти файлы, так как они бессмысленны?(y/n):\n"))
        if choice == "y":
            for file in invalid_files:
                if file in os.listdir(path):
                    print("Удаляю файл: ", file)
                    os.remove(path + r"\\" + file)
        else:
            print("Ну ладно")
    else:
        print("Для каждого файла существует действительная разметка. Все в порядке!")


# функция нумерует все оставшиеся файлы в формате 000001 в порядке возрастания
def set_numbers(path):
    start = int(input("Хорошо. А с какого числа начать нумерацию?\n"))
    if start is not None:
        print("Отличный выбор!")
    j = start
    files = os.listdir(path)
    if "temp" in files:
        files.remove("temp")
    # Создаем резервную папку
    try:
        os.makedirs(path + '/temp')
    except:
        pass
    for i, file in enumerate(files):
        extention = file[-4:]
        copy(path + "/" + file, path + "/temp/") # Копируем файл в резервную папку
        # Переименовываем файлы в резервной папке в соответствии с номером, который ввёл пользователь
        if i % 2 != 0:
            os.rename(path + "/temp/" + file, path + "/temp/" + "{:06}".format(j) + extention)
            j += 1
        else:
            os.rename(path + "/temp/" + file, path + "/temp/" + "{:06}".format(j) + extention)
        os.remove(path + "/" + file) # из исходной папки мы их удаляем
    new_files = os.listdir(path + "/temp/")
    for file in new_files:
        os.rename(path + "/temp/" + file, path + "/" + file) # а теперь обратно из резервной папки копируем файлы в исходную
    os.rmdir(path + "/temp/") # удаляем резервную папку
    print("Фух..Файлы были пронумерованы в порядке возрастания!")


# Функция создает файл train.txt в папке data на основе папки data/obj
def create_train_txt(path):
    with open(path + '/train.txt', "w") as f:
        for file in os.listdir(path):
            if file[-4:] == ".jpg":
                f.write("data/obj/" + file+"\n")
    new_path = path[:path.find("data")+4]
    copy(path + "/train.txt", new_path + "/train.txt")
    os.remove(path + "/train.txt")
    print(f"Файл train.txt успешно создан в папке {new_path}")

############################################################################

path = get_path()
while True:
    print("\nПожалуйста, выберите, что хотите сделать: ")
    print("1) Проверь-ка правильность разметки (наличие корректного текстового файла для каждого изображения)")
    print("2) Джарвис, пронумеруй файлы в порядке возрастания")
    print("3) Создай файл train.txt")
    print("4) Все, отдыхай")
    print("Выш выбор: ", end="")
    choice = int(input())
    print('\n')
    if choice == 1:
        invalid_files = rename_to_jpg(path)
        invalid_files = check_if_txt_exists(path, invalid_files)
        delete_invalid_files(invalid_files, path)
        time.sleep(1)
    elif choice == 2:
        set_numbers(path)
        time.sleep(1)
    elif choice == 3:
        create_train_txt(path)
    elif choice == 666:
        wow()
    else:
        print("Всего хорошего, мистер Старк! Был рад служить.")
        break
