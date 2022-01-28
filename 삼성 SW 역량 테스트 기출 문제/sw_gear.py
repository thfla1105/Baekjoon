from collections import deque

gears=[deque(map(int,input())) for _ in range(4)]
k=int(input())
rt=[list(map(int,input().split())) for _ in range(k)]

score=0

for gear,dir in rt:
  g=gear-1
  tmp1=gears[g][2]
  tmp2=gears[g][6] 
  d=dir
  for i in range(g-1,0-1,-1):
    if tmp2!=gears[i][2]:
      tmp2=gears[i][6]
      d*=-1
      gears[i].rotate(d)
    else:
      break
  d=dir
  for i in range(g+1,4):
    if tmp1!=gears[i][6]:
      tmp1=gears[i][2]
      d*=-1
      gears[i].rotate(d)
    else:
      break
  gears[g].rotate(dir)

for i in range(4):
  if gears[i][0]==1:
    score+=(2**i)

print(score)