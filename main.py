def is_prime(num):
    """判断一个数是否为质数"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def PrimeList(N):
    """输出小于N的所有质数，以空格分隔"""
    primes = [str(num) for num in range(2, N) if is_prime(num)]
    return ' '.join(primes)

# 测试示例
n = int(input("请输入整数N："))
print(PrimeList(n))
    
