def is_prime_factor(num):
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    while num % 5 == 0:
        num //= 5
    return num == 1

def sum_special_numbers(n):
    total_sum = 0
    for i in range(2, n + 1):
        if is_prime_factor(i):
            total_sum += i
    return total_sum


n = int(input())

# 計算結果並輸出
result = sum_special_numbers(n)
print(result)
