#  ------ Initialised global ------

winner = None
string = 'XOOOXOXXO'
lst = [i for i in string]


#  ------ Functions ------

def show(string):  # Show up elements
    view = ((string[i:i + 3]) for i in range(0, len(string), 3))
    print('---------')
    for v in view:
        print('|', end=' ')
        print(' '.join(v), end=' |\n')
    print('---------')


def check_rows():
    row_1 = lst[0] == lst[1] == lst[2] != '_'
    row_2 = lst[3] == lst[4] == lst[5] != '_'
    row_3 = lst[6] == lst[7] == lst[8] != '_'
    if row_1 or row_2 or row_3:
        if row_1:
            return lst[0]
        if row_2:
            return lst[3]
        if row_3:
            return lst[6]
    return False


def check_columns():
    col_1 = lst[0] == lst[3] == lst[6] != '_'
    col_2 = lst[1] == lst[4] == lst[7] != '_'
    col_3 = lst[2] == lst[5] == lst[8] != '_'
    if col_1 or col_2 or col_3:
        if col_1:
            return lst[0]
        if col_2:
            return lst[1]
        if col_3:
            return lst[2]
    return False


def check_diagonals():
    diag_1 = lst[0] == lst[4] == lst[8] != '_'
    diag_2 = lst[2] == lst[4] == lst[6] != '_'
    if diag_1 or diag_2:
        if diag_1:
            return lst[0]
        if diag_2:
            return lst[2]
    return False


#  ------ Launch ------

show(string)
winner = check_rows()
if winner:
    print(f'{winner} is win!')
elif
