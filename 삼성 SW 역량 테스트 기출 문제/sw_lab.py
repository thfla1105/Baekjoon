from collections import deque
import copy

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

max_val=0

def bfs():
  global max_val
  virus=deque()
  graph=copy.deepcopy(board)
  for i in range(n):
    for j in range(m):
      if graph[i][j]==2:
        virus.append([i,j])
  while virus:
    y,x=virus.popleft()
    for i in range(4):
      ny,nx=dy[i]+y,dx[i]+x
      if 0<=ny<n and 0<=nx<m:
        if graph[ny][nx]==0:
          graph[ny][nx]=2
          virus.append([ny,nx])
  max_val=max(max_val,sum(list(x.count(0) for x in graph)))
      

def create_walls(cnt):
  if cnt==3:
    bfs()
    return
  else:
    for i in range(n):
      for j in range(m):
        if board[i][j]==0:
          board[i][j]=1
          create_walls(cnt+1)
          board[i][j]=0

create_walls(0)
print(max_val)