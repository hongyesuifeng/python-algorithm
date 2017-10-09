def select_sort(lists):
    length = len(lists)
    for i in range(length):
        min = i
        for j in range(i+1,length):
            if lists[i] > lists[j]:
                min = j
                lists[i], lists[min] = lists[min], lists[i]
    return lists


if __name__ == '__main__':
    lists = [3,2,4,5,6,1,3,4,6,4]
    print(select_sort(lists))
