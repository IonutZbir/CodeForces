# https://codeforces.com/contest/1520/problem/A

def get_input() -> list:
    tests = int(input())
    inputs = []
    for _ in range(tests):
        n = input()
        string = input()
        
        inputs.append(string)
    return inputs

def solve(string: str) -> str:
    n = len(string)
    for i in range(n - 1):
        if string[i] != string[i + 1]:
            res = check(string[i], string[i + 1:])
            if res:
                return "NO"
    return "YES"

def check(char: str, string: str) -> bool:
    return char in string    

inp = get_input()
for string in inp:
    res = solve(string)
    print(res)