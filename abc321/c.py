k = int(input())

queue = [str(i+1) for i in range(9)]

for q in queue:
    for i in range(int(q[-1])):
        queue.append(q + str(i))
    if len(queue) >= k:
        break

print(queue[k - 1])
