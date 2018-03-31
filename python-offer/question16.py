#数值的整数次方

def power(base, exponent):
    if(abs(base - 0) < 0.1 ** 18 and exponent < 0 ):
        return False
    if exponent < 0:
        abs_exponent = -exponent
        result = 1 / power_positive_exponent2(base, abs_exponent)
        return result
    else:
        return power_positive_exponent2(base,exponent)

def power_positive_exponent(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result 

def power_positive_exponent2(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    result = power_positive_exponent2(base, exponent>>1)
    result *= result 
    if exponent & 1 == 1:
        result *= base
    return result
    
if __name__ == "__main__":
    print(power(2,3))
    print(power(-2,3))
    print(power(0,3))
    print(power(0,-3))
    print(power(2,-3))
    print(power(-2,-3))
