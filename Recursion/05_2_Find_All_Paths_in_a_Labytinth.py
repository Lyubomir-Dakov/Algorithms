r = int(input())
c = int(input())
labyrinth = [list(input()) for row in range(r)]


# [     0    1    2
#     ['-', '-', '-'],    0
#     ['-', '*', '-'],    1
#     ['-', '-', 'e']     2
# ]


def find_path(row, col, lab, direction, path):
    if not in_boundaries(row, col, lab):
        return

    if exit_lab(row, col, lab):
        path.append(direction)
        print(''.join(path).strip())
        path.pop()
        return

    elif is_free(row, col, lab):
        mark_field(row, col, lab)
        path.append(direction)

        find_path(row, col - 1, lab, 'L', path)
        find_path(row, col + 1, lab, 'R', path)
        find_path(row - 1, col, lab, 'U', path)
        find_path(row + 1, col, lab, 'D', path)

        un_mark_field(row, col, lab)
        path.pop()


def in_boundaries(x, y, lab):
    if 0 <= x < len(lab) and 0 <= y < len(lab[x]):
        return True
    return False


def exit_lab(x, y, lab):
    if lab[x][y] == 'e':
        return True
    return False


def is_free(x, y, lab):
    if lab[x][y] == '-':
        return True
    return False


def mark_field(x, y, lab):
    lab[x][y] = 'v'
    return lab


def un_mark_field(x, y, lab):
    lab[x][y] = '-'
    return lab


find_path(0, 0, labyrinth, '', [])
