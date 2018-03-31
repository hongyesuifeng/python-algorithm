#剪绳子

def cut_rope(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    products = [0] * (length + 1)
    products[0:4] = 0,1,2,3
    for i in range(4,length+1):
        maximum = 0
        product = 0 
        for j in range(1,i//2+1):
            product = products[j] * products[i-j]
            maximum = max(product,maximum)
        products[i] = maximum
    maximum = products[length]
    print(products)
    return maximum

if __name__ == "__main__":
    print(cut_rope(0))
    print(cut_rope(3))
    print(cut_rope(5))
    print(cut_rope(8))
