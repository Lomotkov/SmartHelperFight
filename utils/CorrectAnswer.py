def correct_name_end(name):
    if name[-2:] == 'ой':
        return name[0:-2] + 'а'
    if name[-2:] == 'ей':
        return name[0:-2] + 'я'
    if name[-2:] == 'ем':
        return name[0:-2] + 'ь'
    if name[-2:] == 'ом':
        return name[0:-2] + ''
    return name