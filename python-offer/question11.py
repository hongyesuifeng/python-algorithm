#旋转数组的最小数字

def rotate_list(list_number):
    rotate_list = list_number
    index1 = 0
    index2 = len(rotate_list) - 1
    while rotate_list[index1] >= rotate_list[index2]:
        if index2 - index1 == 1:
            index_middle = index2
            break
        index_middle = int(index1/2 + index2/2)
        if rotate_list[index_middle] >= rotate_list[index1]:
            index1 = index_middle
        elif rotate_list[index_middle] <= rotate_list[index2]:
            index2 = index_middle
    return rotate_list[index_middle]

if __name__ == "__main__":
    print(rotate_list([3,4,5,1,2]))
    print(rotate_list([4,5,7,3,4]))
    print(rotate_list([1,1,1,0,0]))

    
    
