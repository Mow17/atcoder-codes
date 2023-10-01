n = str(input())

ans = "Yes"
if (len(n)) == 0:
  ans
else:
  for i in range(len(n) - 1):
    if (int(n[i]) > int(n[i+1])):
      continue
    else:
      ans = "No"
      break

print(ans)
