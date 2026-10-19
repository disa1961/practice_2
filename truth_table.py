def truth_table(n):
    return [
        tuple((i >> bit) & 1 for bit in range(n - 1, -1, -1))
        for i in range(2 ** n)
]
