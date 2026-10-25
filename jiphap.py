import random

random.seed(5)

universe = list(range(200_000))

A = set(random.sample(universe, 80_000))
B = set(random.sample(universe, 20_000))
C = set(random.sample(universe, 5_000))

def intersection_counted(X, Y):
    if len(X) <= len(Y):
        small, large = X, Y
    else:
        small, large = Y, X

    result = set()
    checks = 0

    for x in small:
        checks += 1

        if x in large:
            result.add(x)

    return result, checks


orders = [
    ("A ∩ B ∩ C", A, B, C),
    ("A ∩ C ∩ B", A, C, B),
    ("B ∩ C ∩ A", B, C, A),
]

for name, X, Y, Z in orders:
    first, checks1 = intersection_counted(X, Y)
    result, checks2 = intersection_counted(first, Z)

    print(f"[ {name} ]")
    print(f"중간: {len(first):,}개")
    print(f"총 검사: {checks1 + checks2:,}회")
    print(f"결과: {len(result):,}개")
    print()