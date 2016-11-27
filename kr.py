#!/usr/bin/env python3

def check_win(arr, a):
  for i in range(3):
    if (arr[0][i] == a) and (arr[1][i] == a) and (arr[2][i] == a):
      return True
    if (arr[i][0] == a) and (arr[i][1] == a) and (arr[i][2] == a):
      return True
  if (arr[0][0] == a) and (arr[1][1] == a) and (arr[2][2] == a):
    return True
  if (arr[0][2] == a) and (arr[1][1] == a) and (arr[2][0] == a):
    return True    
  return False


arr = [[], [], []]

count_x = 0
count_o = 0

for i in range(3):
  for j in input().lower():
    if j == 'x':
      count_x+= 1
    elif j == 'o':
      count_o+= 1
    arr[i].append(j)

win_x = check_win(arr, 'x')
win_o = check_win(arr, 'o')

answ = 'NO'

if win_x:
  if count_x == count_o + 1:
    answ = 'YES'
elif win_o:
  if count_x == count_o:
    answ = 'YES'
else:
  if count_x == count_o:
    answ = 'YES'
  if count_x == count_o + 1:
    answ = 'YES'
if win_x and win_o:
  answ = 'NO'

print(answ)    
