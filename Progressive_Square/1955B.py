# https://codeforces.com/problemset/problem/1955/B

import pprint as pp

def get_input() -> list:
    tests = int(input())
    inputs = []
    for _ in range(tests):
        n, c, d = input().split(" ")
        arr_as_strings = input().split(" ")
        arr = [int(num) for num in arr_as_strings]
        
        inputs.append((int(n), int(c), int(d), arr))
    return inputs
    

def create_progressive_square(n: int, a_11: int, c: int, d: int) -> list:
    m = [[0] * n for _ in range(n)]
    b = []
    
    m[0][0] = a_11
    
    for i in range(n - 1):
        for j in range(n):
            m[i + 1][j] = m[i][j] + c
            
    for i in range(n):
        for j in range(n - 1):
            m[i][j + 1] = m[i][j] + d
    
    for i in range(n):
        for j in range(n):
            b.append(m[i][j])

    b.sort()
    return b

def check(a: list, b: list):
    n = len(a)
    for i in range(n):
        if a[i] != b[i]:
            return "NO"
    return "YES"

inp = get_input()
pp.pprint(inp)
for n, c, d, arr in inp:
    arr.sort()
    b = create_progressive_square(n, arr[0], c, d)
    res = check(arr, b)
    #print(res)

