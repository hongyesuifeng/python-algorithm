#调整数组顺序使奇数位于偶数前面

def reorder_odd_even(number_list):
    odd_list = []
    even_list = []
    for i,number in enumerate(number_list):
        print("this is number_list:",number_list)
        if number & 1 == 1:
            odd_list.append(number)
        else:
            even_list.append(number)
    odd_list.extend(even_list)
    return odd_list


if __name__ == "__main__":
    print(reorder_odd_even([1,2,3,4,5]))
    print(reorder_odd_even([3,2,2,5,2,1,3,4]))
    print(reorder_odd_even([]))
    print(reorder_odd_even([1,3,5,7,2,4,6,8]))
    print(reorder_odd_even([2,4,6,8,1,3,5,7]))

    
