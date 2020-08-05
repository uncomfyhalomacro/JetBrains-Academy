reference = {
    (1, 1): 6,
    (1, 2): 3,
    (1, 3): 0,
    (2, 1): 7,
    (2, 2): 4,
    (2, 3): 1,
    (3, 1): 8,
    (3, 2): 5,
    (3, 3): 2
}
which = 0  # helps identify which player it is now

def board(*args):
    user_input = '_________' if args == () else args[0]
    array = [user_input[0:3], user_input[3:6], user_input[6:9]]
    print('---------')
    for ind in array:
        print("| {} {} {} |".format(*ind))
    print('---------')
    return user_input


def check_condition(data):
    array_check = [[data[j + i * 3] for j in range(3)] for i in range(3)]
    array_check.append([array_check[i][j] for j in range(3) for i in range(3) if i == j])
    array_check.append([array_check[i][2 - i] for i in range(3)])
    array_check.extend([[array_check[j][i] for j in range(3)] for i in range(3)])
    condition = None
    if '_' not in data:
        condition = 'Draw'
    elif '_' in data:
        condition = 'Game not finished'
    for i in array_check:
        if ''.join(i).count('X') == 3 or ''.join(i).count('O') == 3:
            condition = "X wins" if ''.join(i).count('X') == 3 else "O wins"

    if abs(data.count('X') - data.count('O')) >= 2:
        condition = "Impossible"
    # print(array_check)
    return condition


def enter_coordinate():
    previous = list(board())
    global which
    while check_condition(''.join(previous)) == 'Game not finished':
        try:
            row, rcol = map(int, input("Enter the coordinates: ").split())  # rcol for reversed column
            if rcol <= 3 and row <= 3:
                for co, i_ in reference.items():
                    if (row, rcol) == co:
                        if previous[i_] in ('X', 'O'):
                            print("This cell is occupied! Choose another one!")
                            break
                        else:
                            if which % 2 == 0:
                                previous[i_] = 'X'
                                board(''.join(previous))
                                which += 1
                                break
                            else:
                                previous[i_] = 'O'
                                board(''.join(previous))
                                which += 1
                                break
            else:
                print("Coordinates should be from 1 to 3!")
        except ValueError:
            print("You should enter numbers!")
    # print(''.join(previous))
    condition = check_condition(''.join(previous))
    print(condition)


def main():
    enter_coordinate()


if __name__ == '__main__':
    main()
