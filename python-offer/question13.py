#机器人的运动范围

def moving_count(threshold, rows, cols):
    if threshold < 0 or rows <= 0 or cols <= 0:
        return 0
    visit = [False] * rows * cols
    count = moving_count_core(threshold, rows, cols, 0, 0, visit)
    return count

def moving_count_core(threshold, rows, cols, row, col, visit):
    count = 0
    if check(threshold, rows, cols, row, col, visit):
        visit[row * cols + col] = True
        count = 1 + moving_count_core(threshold, rows, cols, row - 1, col, visit) + moving_count_core(threshold, rows, cols, row + 1, col, visit) + moving_count_core(threshold, rows, cols, row, col + 1, visit) + moving_count_core(threshold, rows, cols, row, col - 1, visit)
    return count

def check(threshold, rows, cols, row, col, visit):
    if row >= 0 and row < rows and col >= 0 and col < cols and get_digit_sum(row) + get_digit_sum(col) <= threshold and not visit[row*cols + col]:
        return True
    return False

def get_digit_sum(number):
    total_number = 0
    while number > 0:
        total_number += number%10
        number /= 10
    return total_number

if __name__ == "__main__":
    print(moving_count(4,6,6))
