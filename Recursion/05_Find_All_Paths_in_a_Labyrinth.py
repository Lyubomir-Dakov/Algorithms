r = int(input())
c = int(input())
l = [list(input()) for row in range(r)]

result = []


def in_boundaries(row, cow, lab):
    if row < 0 or row >= len(lab) or cow < 0 or cow >= len(lab[row]):
        return False
    return True


def exit_lab(row, cow, lab, direction, path):
    if lab[row][cow] == 'e':
        path.append(direction)
        return True
    return False


def if_free(row, cow, lab):
    if lab[row][cow] == '-':
        return True
    return False


def mark_field(row, cow, direction, path, lab):
    path.append(direction)
    lab[row][cow] = 'v'
    return lab


def un_mark_field(row, cow, lab):
    lab[row][cow] = '-'
    return lab


def find_path(row, cow, direction, path, lab):
    if not in_boundaries(row, cow, lab):
        return

    if exit_lab(row, cow, lab, direction, path):
        print(''.join(path))
        path.pop()
        return
    elif if_free(row, cow, lab):
        mark_field(row, cow, direction, path, lab)
        find_path(row - 1, cow, 'U', path, lab)
        find_path(row + 1, cow, 'D', path, lab)
        find_path(row, cow + 1, 'R', path, lab)
        find_path(row, cow - 1, 'L', path, lab)
        un_mark_field(row, cow, lab)
        path.pop()


find_path(0, 0, '', [], l)
