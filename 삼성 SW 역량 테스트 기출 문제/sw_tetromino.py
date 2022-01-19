n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
visited=[[False]*m for _ in range(n)]
answer=0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(cnt,tmp,r,c):
  global n,m,board,visited,answer
  if cnt==4:
    answer=max(answer,tmp)
    return
  if tmp+max_val*(4-cnt)<=answer:
    return
  for i in range(4):
      nr,nc=r+dx[i],c+dy[i]
      if 0<=nr<n and 0<=nc<m and not visited[nr][nc]:
        visited[nr][nc]=True
        if cnt==2:
          dfs(cnt+1,tmp+board[nr][nc],r,c)
        dfs(cnt+1,tmp+board[nr][nc],nr,nc)
        visited[nr][nc]=False

max_val=max(map(max,board))

for i in range(n):
  for j in range(m):
    visited[i][j]=True
    dfs(1,board[i][j],i,j)
    visited[i][j]=False

print(answer)