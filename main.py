def PrimeList(N):
    if N <= 2:
        return ""
    
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    primes = []
    for i in range(2, N):
        if is_prime(i):
            primes.append(str(i))
    
    return " ".join(primes)

# 测试示例
if __name__ == "__main__":
    # 测试用例
    print(PrimeList(10))  # 输出: 2 3 5 7
    print(PrimeList(20))  # 输出: 2 3 5 7 11 13 17 19
    print(PrimeList(2))   # 输出: (空字符串)
    print(PrimeList(30))  # 输出: 2 3 5 7 11 13 17 19 23 29
