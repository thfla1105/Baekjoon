from collections import deque
import sys
input = sys.stdin.readline

n,m=map(int,input().split())
dt = []
for i in range(n):
  dt.append(list(input()))
  for j in range(m):
    if dt[i][j]=='R':
      rx,ry=i,j
    elif dt[i][j]=='B':
      bx,by=i,j

dx = [-1,1,0,0]
dy =[0,0,-1,1]

def bfs(rx,ry,bx,by):
  dq= deque()
  dq.append((rx,ry,bx,by))
  check = []
  check.append((rx,ry,bx,by))
  cnt =0
  answer=-1
  while dq:
    for i in range(len(dq)):
      rx,ry,bx,by = dq.popleft()
      if cnt>10:
        print(-1)
        return
      if dt[rx][ry] =='O':
        print(cnt)
        return
      for i in range(4):
        drx,dry=rx,ry
        while True:
          drx+=dx[i]
          dry+=dy[i]
          if dt[drx][dry]=='#':
            drx-=dx[i]
            dry-=dy[i]
            break
          if dt[drx][dry]=='O':
            break
        dbx,dby = bx, by
        while True:
          dbx+=dx[i]
          dby+=dy[i]
          if dt[dbx][dby]=='#':
            dbx-=dx[i]
            dby-=dy[i]
            break
          if dt[dbx][dby]=='O':
            break
        if dt[dbx][dby]=='O':
          continue
        if drx==dbx and dry==dby:
          if abs(drx-rx)+abs(dry-ry)> abs(dbx - bx) + abs(dby - by):
            drx-=dx[i]
            dry-=dy[i]
          else:
            dbx-=dx[i]
            dby-=dy[i]
        if (drx,dry,dbx,dby) not in check:
          dq.append((drx,dry,dbx,dby))
          check.append((drx,dry,dbx,dby))
    cnt+=1
  print(-1)
  return
bfs(rx,ry,bx,by)
