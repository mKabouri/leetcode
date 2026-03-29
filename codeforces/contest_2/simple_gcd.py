import math

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        max_ops = 0
        if n > 1:
            if a[0] > math.gcd(a[0], a[1]):
                max_ops += 1
                
            for i in range(1, n - 1):
                g1 = math.gcd(a[i-1], a[i])
                g2 = math.gcd(a[i], a[i+1])
                lcm = (g1*g2)//math.gcd(g1, g2)
                if a[i] > lcm:
                    max_ops += 1

            if a[-1] > math.gcd(a[-2], a[-1]):
                max_ops += 1

        print(max_ops)