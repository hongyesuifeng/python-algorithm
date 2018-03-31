#斐波那契数列

def Fibonacci(n):
    Fn = 0
    F1 = 0
    F2 = 1
    for i in range(n):
        Fn = F1 + F2
        F1 = F2
        F2 = Fn
    return Fn


if __name__ == "__main__":
    print(Fibonacci(0))
    print(Fibonacci(1))
    print(Fibonacci(5))
    print(Fibonacci(7))
    print(Fibonacci(8))
    print(Fibonacci(10))
    
