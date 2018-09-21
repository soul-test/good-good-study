num = [1,34,33,11,22,8,6]
i=0
c=0
while i < 6:
  b = i + 1
  if num[i] < num[b] and c < num[b]:
     c=int(num[b])
  i = i + 1
print(c)
