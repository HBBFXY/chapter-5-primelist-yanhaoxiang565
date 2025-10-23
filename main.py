def PrimeList(N):
    primes = []
    # 遍历2到N-1的数，判断是否为质数
    for num in range(2, N):
        is_prime = True
        # 只需检查到num的平方根，若num能被i整除，不是质数
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(num))
    # 将质数列表用空格连接成字符串
    return " ".join(primes)

# 测试示例
n = 10
result = PrimeList(n)
print(result)
