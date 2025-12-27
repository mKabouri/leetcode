if __name__ == "__main__":
    n = int(input())
    strings = [
        input().strip() for _ in range(n)
    ]
    for string in strings:
        y = 0
        ok = True
        for c in string:
            if c == 'Y':
                y += 1
                if y > 1:
                    print("NO")
                    ok = False
                    break
        if ok:
            print("YES")
