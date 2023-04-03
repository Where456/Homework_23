def filters(file, cmd, value):
    if cmd == 'filter':
        return list(filter(lambda d: value in d, file))
    if cmd == 'map':
        return list(map(lambda d: d.split()[int(value)], file))
    if cmd == 'unique':
        return list(set(file))
    if cmd == 'sort':
        reverse = value == 'asc'
        return sorted(file, reverse=reverse)
    if cmd == 'limit':
        return [i for i in file[:int(value)]]

#
# print(filters(cmd='filter', value='GET', file='"'))