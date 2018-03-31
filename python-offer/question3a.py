def find_duplicate(length, array):
    """找出数组中重复的数字"""
    print(array)
    #judge all boundary conditions
    if length <= 0 or any(x>=length for x in array) or any(x<0 for x in array) < 0:
        return False
    for index,number in enumerate(array):
        while(array[index] != index):
            if array[index] == array[array[index]]:
                return array[index]
            else:
               t = array[index]
               array[index] = array[array[index]]
               array[t] = t
    return False
            
if __name__ == '__main__':
    print(find_duplicate(5,[1,2,3,4,3]))
    print(find_duplicate(5,[0,1,2,3,4]))
    print(find_duplicate(5,[1,2,7,1,2]))
