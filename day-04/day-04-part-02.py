from common.common import read_file


def get_numbers(lines):
    numbers = lines[0]
    numbers = numbers.split(',')
    numbers = [int(number) for number in numbers]
    return numbers


def get_boards(lines):
    lines = lines[2:]
    boards = []

    lines = [line for line in lines if line != '']

    board_count = len(lines) // 5

    for i in range(board_count):
        board = []
        for j in range(i * 5, i * 5 + 5):
            board_line = lines[j]
            board_line = board_line.split()
            board_line = [int(number) for number in board_line]
            board.append(board_line)
        boards.append(board)

    return boards


def init_marks(boards):
    marks = []

    for board in boards:
        board_mark = []
        for line in board:
            board_line_mark = [0] * len(line)
            board_mark.append(board_line_mark)
        marks.append(board_mark)

    return marks


def init_winners(boards):
    winners = {}

    for i in range(len(boards)):
        winners[i] = 0
    return winners


def get_score(number, board, mark_board):
    for row_idx, mark_row in enumerate(mark_board):
        for colum_idx, mark_value in enumerate(mark_row):
            if mark_value == 1:
                board[row_idx][colum_idx] = 0
    unmarked_sum = sum(sum(board, []))
    return number * unmarked_sum


def check_rows(mark_board):
    for row in mark_board:
        if all(elem == 1 for elem in row):
            return True
    return False


def check_columns(mark_board):
    for column_idx in range(len(mark_board[0])):
        all_ones = True
        for row in mark_board:
            if row[column_idx] == 0:
                all_ones = False
        if all_ones:
            return True
    return False


def play_bingo(lines):
    numbers = get_numbers(lines)
    boards = get_boards(lines)
    marks = init_marks(boards)
    winners = init_winners(boards)

    for number in numbers:
        for board_idx, board in enumerate(boards):
            for row_idx, row in enumerate(board):
                for colum_idx, cell_value in enumerate(row):
                    if number == cell_value:
                        marks[board_idx][row_idx][colum_idx] = 1
        for marks_idx, mark_board in enumerate(marks):
            if check_rows(mark_board) or check_columns(mark_board):
                winners[marks_idx] = 1
                if sum(winners.values()) == len(boards):
                    return get_score(number, boards[marks_idx], mark_board)


def main():
    lines = read_file('day-04.txt')

    score = play_bingo(lines)

    print(f'{score=}')


if __name__ == '__main__':
    _lines = read_file('day-04-test.txt')

    loser = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    row_winner = [[1, 1, 1], [1, 0, 1], [0, 1, 0]]
    column_winner = [[0, 1, 1], [1, 0, 1], [0, 1, 1]]

    assert get_numbers(_lines) == [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8,
                                   19, 3, 26, 1]
    assert len(get_boards(_lines)) == 3
    assert len(get_boards(_lines)[0]) == 5
    assert len(get_boards(_lines)[0][0]) == 5
    assert len(init_marks(get_boards(_lines))) == 3
    assert len(init_marks(get_boards(_lines))[0]) == 5
    assert len(init_marks(get_boards(_lines))[0][0]) == 5
    assert len(init_winners(get_boards(_lines)).keys()) == 3
    assert check_rows(loser) is False
    assert check_rows(row_winner) is True
    assert check_columns(loser) is False
    assert check_columns(column_winner) is True

    assert play_bingo(_lines) == 1924

    main()
