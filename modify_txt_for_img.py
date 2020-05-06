from Win_to_linux_endings import modify


def delete_last_line(path):
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
        f.close()
    with open(path, "w") as f:
        for line in lines:
            f.write(line)


"""
Убирает длинный конец строки в train.txt
"""
with open(r"C:\CREESTL\Programming\PythonCoding\AlexeyABfork\darknet-master\build\darknet\x64\data\obj\names.txt") as names:
    lines = names.readlines()
    for line in lines:
        if line[0] == "n":
            continue
        part = line[:6]
        new_line = "C:\\CREESTL\\Programming\\PythonCoding\\AlexeyABfork\\darknet-master\\build\\darknet\\x64\\data\\obj\\" + part + ".txt"
        print(new_line)
        try:
            modify(new_line)
            try:
                delete_last_line(new_line)
            except:
                continue
        except FileNotFoundError:
            print("NO FILE " + new_line)


