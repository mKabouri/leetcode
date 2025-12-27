def greedy(niceness, X):
    if len(niceness) <= 1:
        return X
    else:
        option1 = greedy(niceness[1:], X + niceness[0])
        el2 = niceness[1]
        niceness.pop(1)
        option2 = greedy(niceness.copy(), X - el2)
        return max(option1, option2)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(greedy(a, 0))
