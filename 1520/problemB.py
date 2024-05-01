# https://codeforces.com/contest/1520/problem/B

def get_input() -> list:
    tests = int(input())
    inputs = []
    for _ in range(tests):
        n = input() 
        inputs.append(int(n))
    return inputs

def solve(n: int) -> int:
    len_n = len(str(n))
    numbers = []
    for i in range(1, len_n + 1):
        for j in range(1, 10):
            numbers.append(int(str(j) * i))
    c = 0
    for i in numbers:
        c += 1 if i <= n else 0
    return c
    
inp = get_input()
for n in inp:
    res = solve(n)
    print(res)
