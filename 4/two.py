"""4/1 adventofcode"""

with open("input.txt", "r", encoding="UTF-8") as i_file:
    data = i_file.read().splitlines()
    numbers = list(map(int, data[0].split(",")))
    boards = []

    for i in range(2, len(data), 6):
        board = []
        for y in range(5):
            if data[i + y][0] == " ":
                board.append(
                    list(map(int, data[i + y][1:].replace("  ", " ").split(" ")))
                )
            else:
                board.append(list(map(int, data[i + y].replace("  ", " ").split(" "))))
        boards.append(board)


def complete_check(input_board: list) -> bool:
    """Checks if someone wins"""

    # Linear
    for board_line in input_board:
        if board_line.count("X") == 5:
            return True

    # Vertical
    for num in range(5):
        column = []
        for board_line in input_board:
            column.append(board_line[num])
        if column.count("X") == 5:
            return True

    return False


def apply_num(input_board: list, input_num: int) -> None:
    """Replaces certain number in board with X char"""

    for board_line in input_board:
        for i in range(5):
            if board_line[i] == input_num:
                board_line[i] = "X"


def sum_non_x(input_board: list) -> int:
    """Sums all non marked numbers in board"""

    total = 0
    for board_line in input_board:
        total += sum([0 if board_line[i] == "X" else board_line[i] for i in range(5)])
    return total

for chosen_num in numbers:
    for board in boards:
        apply_num(board, chosen_num)
    for board in boards:
        if complete_check(board):
            if len(boards) == 1:
                print(chosen_num, sum_non_x(board))
                print(f"\nVyherce >> {chosen_num*sum_non_x(board)}")
                exit()
            else:
                boards.remove(board)
