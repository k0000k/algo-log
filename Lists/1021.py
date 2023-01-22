from collections import deque

N, cnt = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque([i for i in range(1, N + 1)])

operation_cnt = 0
for target in targets:
    if (dq[0] == target):
        dq.popleft()
    else:
        temp_cnt = min(dq.index(target), len(dq) - dq.index(target))
        operation_cnt += temp_cnt

        if (temp_cnt == dq.index(target)):
            for i in range(temp_cnt):
                dq.append(dq.popleft())
            dq.popleft()
        else:
            for i in range(temp_cnt):
                dq.appendleft(dq.pop())
            dq.popleft()

print(operation_cnt)
