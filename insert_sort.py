def insert_sort(lists):
    length = len(lists)
    for i in range(1,length):
        key = lists[i]
        j = i - 1
        while j>=0 and lists[j] > key:
            lists[j+1] = lists[j]
            j -= 1
        lists[j+1] = key
    return lists

if __name__ == '__main__':
    lists = [3,2,4,5,6,1,3,4,6,4]
    print(insert_sort(lists))
