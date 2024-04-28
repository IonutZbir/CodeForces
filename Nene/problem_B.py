# https://codeforces.com/problemset/problem/1956/B

def get_doubles(cards: list[int]) -> list[int]:
    n = len(cards)
    doubles = [0] * max(cards)
    
    for i in cards:
        doubles[i - 1] += 1
    
    #print(doubles)
    return doubles
    

def solution(n: int, cards: list[int]) -> int:
    
    # Il numero di punti è il numero di doppioni pari, perchè inizo per primo il game
    
    # sort the cards
    cards = sorted(cards)
    
    # cards: [1, 1, 2, 2, 3, 4, 10, 11, 11]
    # doubles: [2, 2, 1, 1, 0, 0, 0, 0, 0, 1, 2]
    
    doubles = get_doubles(cards)
    
    points = 0
    for i in doubles:
        points += 1 if (i % 2 == 0 and i != 0) else 0
    
    return points

tests = int(input())
inputs = []
for _ in range(tests):
    n = int(input())
    cards_as_strings = input().split(" ")
    cards = [int(num) for num in cards_as_strings]
    
    inputs.append((n, cards))

# print("\n")

# print(inputs)

# print("\n")

for n, cards in inputs:        
    sol = solution(n, cards)
    print(sol)

