def are_equivalent(f, g, n):
    for i in range(2 ** n):
        row = tuple((i >> bit) & 1 for bit in range(n - 1, -1, -1))
        if f(*row) != g(*row):
            return False
    return True
def implies(a, b):
    return (not a) or b
if __name__ == "__main__":
    print(are_equivalent(
        lambda a, b: not (a and b),
        lambda a, b: (not a) or (not b),
        2
    ))
    print(are_equivalent(
        lambda a, b: not (a or b),
        lambda a, b: (not a) and (not b),
        2
    ))
    print(are_equivalent(
        lambda a, b: implies(a, b),
        lambda a, b: (not a) or b,
        2
    ))
    print(are_equivalent(
        lambda a, b: implies(a, b),
        lambda a, b: implies(not b, not a),
        2
    ))
    print(are_equivalent(
        lambda a, b, c: a and (b or c),
        lambda a, b, c: (a and b) or (a and c),
        3
    ))
