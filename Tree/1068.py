import sys

def dfs(node, tree, result):
    for i in tree[node]:
        if (tree[i] == []):
            result += 1
            continue
        result= dfs(i, tree, result)
    return result

N = int(sys.stdin.readline())
parents = list(map(int, sys.stdin.readline().split()))
remove_node = int(sys.stdin.readline())
tree = {}

for i in range(N):
    tree[i] = []

for i in range(N):
    if (parents[i] == -1):
        continue
    tree[parents[i]].append(i)

for i in range(N):
        if (remove_node in tree[i]):
            del tree[i][tree[i].index(remove_node)]

all_leaf_nodes = 0
for i in range(N):
    if (tree[i] == []):
        all_leaf_nodes += 1

if (tree[remove_node] == []):
    result = 1
    print(all_leaf_nodes - result)
elif (parents.index(-1) == remove_node):
    print(0)
else:
    result = 0
    result = dfs(remove_node, tree, result)
    print(all_leaf_nodes - result)
