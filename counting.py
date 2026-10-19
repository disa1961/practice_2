def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def arrangements(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    result = 1
    for i in range(n - k + 1, n + 1):
        result *= i
    return result
def combinations(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    return result
