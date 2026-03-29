if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(*range(1, n+1)[::-1])
