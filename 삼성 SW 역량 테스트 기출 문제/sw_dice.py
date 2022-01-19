import sys
input=sys.stdin.readline

n,m,x,y,k=map(int,input().split())
board=[list(map(int, input().split())) for _ in range(n)]
direction=list(map(int, input().split()))
dice=[0]*7 #상북동서남하

dx=[0,0,-1,1] #동서북남
dy=[1,-1,0,0]

def move(dir, arr):  # 주사위 변화
    if dir==1:    # 동
        return [0, arr[4], arr[2], arr[1], arr[6], arr[5], arr[3]]
    elif dir==2:  # 서
        return [0, arr[3], arr[2], arr[6], arr[1], arr[5], arr[4]]
    elif dir==3:  # 북
        return [0, arr[5], arr[1], arr[3], arr[4], arr[6], arr[2]]
    elif dir==4:  # 남
        return [0, arr[2], arr[6], arr[3], arr[4], arr[1], arr[5]]

for d in direction:
  if 0<=x+dx[d-1]<n and 0<=y+dy[d-1]<m:
    x,y=x+dx[d-1],y+dy[d-1]
    dice=move(d,dice)
    if board[x][y]==0:
      board[x][y]=dice[6]
    else:
      dice[6],board[x][y] = board[x][y],0
    print(dice[1])
  else:
    continue