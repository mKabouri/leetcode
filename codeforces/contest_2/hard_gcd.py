from math import gcd

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        g = [gcd(a[i], a[i + 1]) for i in range(n - 1)]
        l = [0]*n
        l[0] = g[0]
        l[-1] = g[-1]

        for i in range(1, n - 1):
            x = gcd(g[i - 1], g[i])
            l[i] = (g[i - 1]//x) * g[i]

        ans = 0
        for i in range(n):
            if l[i] > b[i]:
                continue

            if l[i] != a[i]:
                ans += 1
                continue

            lim = b[i]//a[i]
            if lim < 2:
                continue
            
            if i > 0:
                left = a[i - 1]//g[i - 1]
            else:
                left = 1
            if i < n - 1:
                right = a[i + 1]//g[i]
            else:
                right = 1

            for k in range(2, lim + 1):
                if gcd(k, left*right) == 1:
                    ans += 1
                    break

        print(ans)
