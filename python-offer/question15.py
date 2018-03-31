#二进制中1的个数

def count_one(number):
    count = 0
    while number:
        number = number & (number - 1)
        count += 1
    return count

if __name__ == "__main__":
    print(bin(1))
    print(count_one(1))
    print(bin(2))
    print(count_one(2))
    print(bin(5))
    print(count_one(5))
    print(bin(6))
    print(count_one(6))
    print(bin(7))
    print(count_one(7))
    print(bin(13))
    print(count_one(13))

