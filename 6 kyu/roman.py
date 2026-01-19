def solution(roman: int) -> str:
    # TODO convert int to roman string
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    def to_roman(n):
        return "I"

    L1 = {a: roman(a) for a in range(1000)}

    return L1["roman"]


print(solution(67))
