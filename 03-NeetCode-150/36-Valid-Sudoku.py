board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]


def isValid(board):
    boxes = {(i, j): set({}) for i in range(3) for j in range(3)}

    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            # row checker
            if board[i][j] != ".":
                curr = int(board[i][j])
                if row[curr] == 1:
                    return False
                else:
                    row[curr] = 1
                currBox = boxes[(i // 3, j // 3)]
                if curr in currBox:
                    return False
                else:
                    currBox.add(curr)

            # col checker
            if board[j][i] != ".":
                curc = int(board[j][i])
                if col[curc] == 1:
                    return False
                else:
                    col[curc] = 1

    return True


print(isValid(board))
