"""
Проверяет, каждая ли фотография размечена

"""
import os

def check_if_txt_not_empty():
    for file in os.listdir("img_reserve/"):
        if file[-3:] == "txt":
            with open("img/" + file) as f:
                if (f.readlines() == []):
                    print("FILE ", file[:-3] + "jpg", "HASN`T BEEN LABELED!")


def check_if_txt_exists():
    files = os.listdir("img/")
    for i in range(0,len(files)-1, 2):
        first = files[i]
        print('first ', first)
        next = files[i+1]
        print('next ', next, "\n")
        if first[:6] == next[:6]:
            pass
        else:
            print("FILE ", first, " HASN`T BEEN LABELED")
            break

check_if_txt_exists()



