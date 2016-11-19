
def mySortKey(inputStr):
  if inputStr[1] == 1:
    return([inputStr[0], 0])
  return([inputStr[0], 1])


N = int(input())

lst = []
for i in range(N):
  a, b = map(int, input().split())
  lst.append((a, 1))
  lst.append((b, -1))

lst.sort(key=mySortKey)

m = 0
s = 0
for i in lst:
  s+= i[1]
  if s > m:
    m = s

print(m)    
