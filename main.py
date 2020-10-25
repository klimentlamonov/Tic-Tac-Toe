#  ------ Initialised global ------

lst = [' ' for i in range(9)]
iterate = 1


#  ------ Functions ------

def show(current_lst):  # Show up elements
    view = ((current_lst[i:i + 3]) for i in range(0, len(current_lst), 3))
    print('---------')
    for v in view:
        print('|', end=' ')
        print(' '.join(v), end=' |\n')
    print('---------')


# def check_impossible():  # Check impossible errors
#     if abs(string.count('X') - string.count('O')) >= 2:
#         print('Impossible')
#         return True
#     elif ((lst[:3].count('X') == 3 or lst[:3].count('O') == 3) and
#           (lst[3:6].count('X') == 3 or lst[3:6].count('O') == 3)) or (
#             (lst[:3].count('X') == 3 or lst[:3].count('O') == 3) and
#             (lst[6:9].count('X') == 3 or lst[6:9].count('O') == 3)) or (
#             (lst[6:9].count('X') == 3 or lst[6:9].count('O') == 3) and
#             (lst[3:6].count('X') == 3 or lst[3:6].count('O') == 3)):
#         print("Impossible")
#         return True
#     elif ((lst[::3].count('X') == 3 or lst[::3].count('O') == 3) and
#           (lst[1::3].count('X') == 3 or lst[1::3].count('O') == 3)) or (
#             (lst[::3].count('X') == 3 or lst[::3].count('O') == 3) and
#             (lst[2::3].count('X') == 3 or lst[2::3].count('O') == 3)) or (
#             (lst[2::3].count('X') == 3 or lst[2::3].count('O') == 3) and
#             (lst[1::3].count('X') == 3 or lst[1::3].count('O') == 3)):
#         print("Impossible")
#         return True
#     return False


# def check_not_finished():
#     if not check_winner() and lst.count(' ') != 0:
#         print("Game not finished")
#         return True
#     return False


def check_winner():  # Check the winner/draw in case of no error
    checkers = (check_rows, check_columns, check_diagonals)
    for check in checkers:
        if check(lst):
            return check(lst)
    return False


def check_rows(current_lst):
    row_1 = current_lst[0] == current_lst[1] == current_lst[2] != ' '
    row_2 = current_lst[3] == current_lst[4] == current_lst[5] != ' '
    row_3 = current_lst[6] == current_lst[7] == current_lst[8] != ' '
    if row_1 or row_2 or row_3:
        if row_1:
            return current_lst[0]
        if row_2:
            return current_lst[3]
        if row_3:
            return current_lst[6]
    return False


def check_columns(current_lst):
    col_1 = current_lst[0] == current_lst[3] == current_lst[6] != ' '
    col_2 = current_lst[1] == current_lst[4] == current_lst[7] != ' '
    col_3 = current_lst[2] == current_lst[5] == current_lst[8] != ' '
    if col_1 or col_2 or col_3:
        if col_1:
            return current_lst[0]
        if col_2:
            return current_lst[1]
        if col_3:
            return current_lst[2]
    return False


def check_diagonals(current_lst):
    diag_1 = current_lst[0] == current_lst[4] == current_lst[8] != ' '
    diag_2 = current_lst[2] == current_lst[4] == current_lst[6] != ' '
    if diag_1 or diag_2:
        if diag_1:
            return current_lst[0]
        if diag_2:
            return current_lst[2]
    return False


'''
    The Matrix presentations:
    (1, 3) (2, 3) (3, 3)
    (1, 2) (2, 2) (3, 2)
    (1, 1) (2, 1) (3, 1)
'''


def put_value(x_val, y_val, flag):
    coordinates = {
        (1, 3): 0, (2, 3): 1, (3, 3): 2,
        (1, 2): 3, (2, 2): 4, (3, 2): 5,
        (1, 1): 6, (2, 1): 7, (3, 1): 8
    }
    coordinate = (x_val, y_val)
    if lst[coordinates[coordinate]] == ' ':
        lst[coordinates[coordinate]] = 'X' if flag % 2 != 0 else 'O'
        return True
    return False


#  ------ Launch ------

show(lst)  # Show the game result

while True:
    try:
        x, y = [i for i in input("Enter the coordinates: ").split()]
        if (not x.isdigit()) or (not y.isdigit()):
            print("You should enter numbers!")
        elif not (0 < int(x) <= 3 and 0 < int(y) <= 3):
            print("Coordinates should be from 1 to 3!")
        else:
            if not put_value(int(x), int(y), iterate):
                print("This cell is occupied! Choose another one!")
            else:
                show(lst)
                if not check_winner():
                    iterate += 1
                    continue
                else:
                    print(check_winner() + " wins")
                    break
    except TypeError:
        continue
