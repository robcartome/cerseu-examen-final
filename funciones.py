def file_manipulation(dir, lista):
    try:
        file = open(dir, 'w')
        for elem in lista:
            file.writelines(elem)
        file.close()
        return file
    except OSError as err:
        print("Error de lectura {}".format(err))