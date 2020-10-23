#  Initialised global

string = 'XOXOXOXOX'
lst = [i for i in string]


#  Functions

def show(string):  # show up elements
    view = ((string[i:i + 3]) for i in range(0, len(string), 3))
    print('---------')
    for v in view:
        print('|', end=' ')
        print(' '.join(v), end=' |\n')
    print('---------')


#  Launch

show(string)
