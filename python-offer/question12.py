#矩阵中的路劲

def has_path(matrix, rows, cols, string):
    if matrix == None or len(matrix) < rows * cols or string == None or len(string) <= 0:
        return False
    visit = [False] * rows * cols
    for i in range(rows):
        for j in range(cols):
            if find_path(matrix, rows, cols, string, i, j, 0, visit):
                return True
    return False 

def find_path(matrix, rows, cols, string, row, col, step, visit):
    if step == len(string):
        return True
    path = False
    if (row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == string[step] and visit[row * cols + col] == False):
        visit[row * cols + col] = True
        step = step + 1
        path = find_path(matrix, rows, cols, string, row, col + 1, step, visit) or find_path(matrix, rows, cols, string, row, col -1 , step, visit) or find_path(matrix, rows, cols, string, row + 1, col, step, visit) or find_path(matrix, rows, cols, string, row - 1, col, step, visit)
        if not path:
            visit[row * cols + col] = False
            step = step - 1
    #print("now is the step: ",step)
    #print("now is the visit: ",visit)
    #print("now is the path: ",path)
    return path


if __name__ == "__main__":
    print("now is the 'bfce': ")
    print(has_path(['a','b','t','g','c','f','c','s','j','d','e','h'],3,4,'bfce'))
    print("now is the 'abfb': ")
    print(has_path(['a','b','t','g','c','f','c','s','j','d','e','h'],3,4,'abfb'))
