# https://codeforces.com/contest/1520/problem/C

def get_input() -> list:
    tests = int(input())
    inputs = []
    for _ in range(tests):
        n = input() 
        inputs.append(int(n))
    return inputs

def adjacent(a: int, b: int) -> bool:
    return abs(a - b)

def solve(n: int) -> int | list[list[int]]:
    mat = [[0] for _ in range(n)]
    range_numers = range(1, (n ** 2) + 1) 
    for r in range(n):
        for c in range(n):
            pass
            

inp = get_input()
for n in inp:
    res = solve(n)
    print(n)