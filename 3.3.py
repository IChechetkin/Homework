def thesaurus(*args):
    new_list = {}
    for name in args:
        key = name[0].capitalize()
        if key not in new_list:
            new_list[key] = []
        new_list[key].append(name)
    return new_list
print(thesaurus('Глеб', 'Илья', 'Евгения', 'Елизавета', 'Михаил', 'Петр', 'Владислав', 'Владимир', 'Анатолий'))