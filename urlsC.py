# Написать функцию, которая примает на вход файл, который содержит urls
# Функция должна прочесть файл построчно и состравить словать.
# Ключапмикоторого будут протоколы (http/https), а значениями сами urls.


with open("urls.txt", 'r') as file:
    urls = {}
    for line in file:
        newline = line[:-2]
        k, *v = newline.split("://")
        urls[k] = v
        print(urls)
        for key in list(urls.keys()):
            if key != 1:
                del urls[key]
            elif urls == " ":
                del urls
                print(urls)
