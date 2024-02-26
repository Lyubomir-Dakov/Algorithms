field = [['-' for y in range(8)] for x in range(8)]


# queen_location = field[r][c]
# queen strikes:
# line     -> field[1-8][c]
# column   -> field[r][1-8]
# diagonal -> field[r+1][c+1] .... field[r-1][c-1] .... field[r+1][c-1] .... field[r-1][c+1]
# r and c in range(0, 8)


def mark_area(field, row, cow, number_of_queens_on_field):
    field[row][cow] = '*'
    number_of_queens_on_field += 1


def un_mark_area(field, row, cow, number_of_queens_on_field):
    field[row][cow] = '-'
    number_of_queens_on_field -= 1


def can_put_queen(field, row, cow):
    queen_locations = []
    hot_fields = []
    for r in range(8):
        for c in range(8):
            if field[r][c] == '*':
                queen_locations.append((r, c))
    for r, c in queen_locations:
        for i in range(8):
            hot_fields.append((i, c))
            hot_fields.append((r, i))
            if r - i >= 0 and c - i >= 0 and not (r - i, c - i) in hot_fields:
                hot_fields.append((r - i, c - i))
            if r - i >= 0 and c + i <= 7 and not (r - i, c + i) in hot_fields:
                hot_fields.append((r - i, c + i))
            if r + i <= 7 and c - i >= 0 and not (r + i, c - i) in hot_fields:
                hot_fields.append((r + i, c - i))
            if r + i <= 7 and c + i <= 7 and not (r + i, c + i) in hot_fields:
                hot_fields.append((r + i, c + i))
    if (row, cow) in hot_fields:
        return False
    return True


def put_8_queens(field, row, cow, number_of_queens_on_field):
    if row < 0 or row >= 8 or cow < 0 or cow >= 8:
        return

    if field[row][cow] == '*':
        return

    if number_of_queens_on_field == 8:
        print(field)
        exit()
        return

    if can_put_queen(field, row, cow):
        mark_area(field, row, cow, number_of_queens_on_field)
    else:
        return

    for i in range(8):
        for j in range(8):
            put_8_queens(field, i, j, number_of_queens_on_field)

    un_mark_area(field, row, cow, number_of_queens_on_field)


put_8_queens(field, 0, 0, 0)
