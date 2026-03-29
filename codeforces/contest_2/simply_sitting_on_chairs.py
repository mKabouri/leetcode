if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))

        max_chairs = 0
        visited = set()
        printed = False
        for i in range(n):
            if i+1 in visited:
                print(max_chairs)
                printed = True
                break
            
            if i + 1 >= p[i]:
                max_chairs += 1
                visited.add(p[i])

        if not printed:
            print(max_chairs)
