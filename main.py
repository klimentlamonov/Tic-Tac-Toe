#  ------ Initialised global ------

string = input()
lst = [i for i in string]


#  ------ Functions ------

def show():  # Show up elements
    view = ((string[i:i + 3]) for i in range(0, len(string), 3))
    print('---------')
    for v in view:
        print('|', end=' ')
        print(' '.join(v), end=' |\n')
    print('---------')


def check_impossible():  # Check impossible errors
    if abs(string.count('X') - string.count('O')) >= 2:
        print('Impossible')
        return True
    elif ((lst[:3].count('X') == 3 or lst[:3].count('O') == 3) and
          (lst[3:6].count('X') == 3 or lst[3:6].count('O') == 3)) or (
            (lst[:3].count('X') == 3 or lst[:3].count('O') == 3) and
            (lst[6:9].count('X') == 3 or lst[6:9].count('O') == 3)) or (
            (lst[6:9].count('X') == 3 or lst[6:9].count('O') == 3) and
            (lst[3:6].count('X') == 3 or lst[3:6].count('O') == 3)):
        print("Impossible")
        return True
    elif ((lst[::3].count('X') == 3 or lst[::3].count('O') == 3) and
          (lst[1::3].count('X') == 3 or lst[1::3].count('O') == 3)) or (
                 (lst[::3].count('X') == 3 or lst[::3].count('O') == 3) and
                 (lst[2::3].count('X') == 3 or lst[2::3].count('O') == 3)) or (
                 (lst[2::3].count('X') == 3 or lst[2::3].count('O') == 3) and
                 (lst[1::3].count('X') == 3 or lst[1::3].count('O') == 3)):
        print("Impossible")
        return True
    return False


def check_not_finished():
    if not check_winner() and lst.count('_') != 0:
        print("Game not finished")
        return True
    return False


def check_winner():  # Check the winner/draw in case of no error
    checkers = (check_rows, check_columns, check_diagonals)
    for check in checkers:
        if check(lst):
            return check(lst)
    return False


def check_rows(current_lst):
    row_1 = current_lst[0] == current_lst[1] == current_lst[2] != '_'
    row_2 = current_lst[3] == current_lst[4] == current_lst[5] != '_'
    row_3 = current_lst[6] == current_lst[7] == current_lst[8] != '_'
    if row_1 or row_2 or row_3:
        if row_1:
            return current_lst[0]
        if row_2:
            return current_lst[3]
        if row_3:
            return current_lst[6]
    return False


def check_columns(current_lst):
    col_1 = current_lst[0] == current_lst[3] == current_lst[6] != '_'
    col_2 = current_lst[1] == current_lst[4] == current_lst[7] != '_'
    col_3 = current_lst[2] == current_lst[5] == current_lst[8] != '_'
    if col_1 or col_2 or col_3:
        if col_1:
            return current_lst[0]
        if col_2:
            return current_lst[1]
        if col_3:
            return current_lst[2]
    return False


def check_diagonals(current_lst):
    diag_1 = current_lst[0] == current_lst[4] == current_lst[8] != '_'
    diag_2 = current_lst[2] == current_lst[4] == current_lst[6] != '_'
    if diag_1 or diag_2:
        if diag_1:
            return current_lst[0]
        if diag_2:
            return current_lst[2]
    return False


#  ------ Launch ------

show()  # Show the game result

if not(check_impossible() or check_not_finished()):
    if not check_winner():
        print('Draw')
    else:
        print(check_winner() + " wins")
