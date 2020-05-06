"""
Возможно он не загружает картинки из за файла train.txt а именно из окончания строк \r\n
Их надо преобразовать просто в \n
"""
def modify(path):
    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'
    with open(path, 'rb') as open_file:
        content = open_file.read()
        content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
    with open(path, 'wb') as open_file:
        open_file.write(content)

modify(r"C:\CREESTL\Programming\PythonCoding\AlexeyABfork\darknet-master\build\darknet\x64\data\train.txt")

