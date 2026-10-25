import random

random.seed(5) # 시드에 1~5 사이 숫자를 차례대로 넣고 결과를 계산해서 평균을 냈습니다.

universe = list(range(200_000))

A = set(random.sample(universe, 80_000))
B = set(random.sample(universe, 20_000))
C = set(random.sample(universe, 5_000))

def gyojiphap(X, Y):
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
    first, checks1 = gyojiphap(X, Y)
    result, checks2 = gyojiphap(first, Z)

    print(f"[ {name} ]")
    print(f"중간: {len(first):,}개")
    print(f"총 검사: {checks1 + checks2:,}회")
    print(f"결과: {len(result):,}개")
    print()
