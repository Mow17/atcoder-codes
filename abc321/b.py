n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = -1
for i in range(101):
  b = a.copy()
  b.append(i)
  b.sort()
  tmp = 0
  for j in range(len(b) - 2):
    tmp += b[j+1]
  if tmp >= x:
    ans = i
    break
print(ans)
