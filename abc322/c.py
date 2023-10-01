n, m = map(int, input().split())
a = list(map(int, input().split()))

k = 0
for i in range(n):
  if a[k] == i + 1:
    print(0)
    k += 1
  else:
    print(a[k] - (i + 1))
