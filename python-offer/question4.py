def find_in_matrix(matrix,number):
    """二维数组中的查找"""
    if matrix:		  
        rows = len(matrix)
        columns = len(matrix[0])
        row = 0
        while(matrix and row<rows and columns>0):
            if matrix[row][columns-1] == number:
                return number
            elif matrix[row][columns-1] > number:
                columns = columns - 1
            elif matrix[row][columns-1] < number:
                row = row + 1
    return False

if __name__ == "__main__":
    matrix1 = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    matrix2 = None
    print(find_in_matrix(matrix1,7))
    print(find_in_matrix(matrix1,5))
    print(find_in_matrix(matrix2,5))

        
