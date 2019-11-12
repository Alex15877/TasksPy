# Написать функцию, которая примает на вход файл, который содержит urls
# Функция должна прочесть файл построчно и состравить словать.
# Ключапмикоторого будут протоколы (http/https), а значениями сами urls.


def urls(file):
    try:
        f = open(file, 'r')
        urls_dict = {'http': [], 'https': []}
        for line in f:
            if line[:5] == 'https':
                urls_dict['https'].append(line[:-2])
            else:
                urls_dict['http'].append(line[:-2])
    except FileNotFoundError:
        print('Файл не найден')
    finally:
        f.close()
    return urls_dict


if __name__ == '__main__':
    print(urls('urls.txt'))