from collections import deque

n,m=map(int,input().split())
board=[list(map(int,input())) for _ in range(n)]

dy=[1,-1,0,0] #상하좌우 
dx=[0,0,1,-1]

def bfs(x,y):
  q=deque()
  q.append((x,y))

  while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m:
          if board[nx][ny]==0:
            continue
          if board[nx][ny]==1:
            q.append((nx,ny))
            board[nx][ny]=board[x][y]+1
  return board[n-1][m-1]
    
print(bfs(0,0))