import sys

sys.setrecursionlimit(10**6)

def find_parent(node, tree, parent):
    for i in tree[node]:
        if (parent[i] == 0):
            parent[i] = node
            find_parent(i, tree, parent)

cnt = int(sys.stdin.readline())
tree = [[] for i in range(cnt + 1)]
parent = [0 for i in range(cnt + 1)]

for i in range(cnt - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
    
find_parent(1, tree, parent)

for i in parent[2:]:
    print(i)
