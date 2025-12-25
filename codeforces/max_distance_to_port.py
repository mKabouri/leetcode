# link: https://codeforces.com/problemset/problem/2172/M

from collections import defaultdict, deque

def compute_distances_to_port(adjacency_dict, n):
    dist = [-1]*n
    queue = deque([0])
    dist[0] = 0
    while queue:
        u = queue.popleft()
        for v in adjacency_dict[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist

def solve(adjacency_dict, product2cities_dict, n):
    dist2port = compute_distances_to_port(adjacency_dict, n)
    
    res = []
    num_products = len(product2cities_dict)
    for product in range(num_products):
        cities = product2cities_dict[product+1]
        res.append(max([dist2port[city] for city in cities]))
    print(*res)

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    products = list(map(int, input().split()))

    product2cities_dict = defaultdict(set)
    for i, product in enumerate(products):
        product2cities_dict[product].add(i)

    adj_dict = defaultdict(set)
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj_dict[u].add(v)
        adj_dict[v].add(u)

    solve(adj_dict, product2cities_dict, n)
