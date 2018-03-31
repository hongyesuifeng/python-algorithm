#顺时针打印矩阵

def print_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0]) if matrix else 0
    start = 0
    print_element = []
    while start * 2 < rows and start * 2 < columns:
        print_circle(matrix, start, rows, columns, print_element)
        start += 1
    print(print_element)

def print_circle(matrix, start, rows, columns, print_element):
    row = rows - start - 1
    column = columns - start - 1
    for c in range(start, column + 1):
        print_element.append(matrix[start][c])
    if start < row:
        for r in range(start + 1, row + 1):
            print_element.append(matrix[r][column])
    if start < row and start < column:
        for c in range(start, column)[::-1]:
            print_element.append(matrix[row][c])
    if start < row and start < column:
        for r in range(start + 1, row)[::-1]:
            print_element.append(matrix[r][start])

if __name__ == "__main__":
    matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix2 = [[1,2,3,4]]
    matrix3 = [[1]] 
    matrix4 = [[1],[2],[3],[7]]
    print_matrix(matrix1)
    print_matrix(matrix2)
    print_matrix(matrix3)
    print_matrix(matrix4)
