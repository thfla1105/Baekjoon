from collections import deque

n=int(input())
m=int(input())
board={i:[] for i in range(1,n+1)}
for _ in range(m):
  k,l=map(int,input().split())
  board[k].append(l)
  board[l].append(k)

def bfs(start):
  visited=[]
  virus=deque()

  virus.append(start)
  while virus:
    tmp=virus.popleft()
    if tmp not in visited:
      visited.append(tmp)
      virus.extend(board[tmp])
  return visited

print(len(bfs(1))-1)