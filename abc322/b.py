n, m = map(int, input().split())
s = str(input())
t = str(input())

head, tale = False, False

# print(t[:n+1])
if t[:n] == s:
  head = True

# print(t[m-1-n:m-1])
if t[m-n:m] == s:
  tale = True

ans = 3
if head and tale:
  ans = 0
elif head:
  ans = 1
elif tale:
  ans = 2

print(ans)
