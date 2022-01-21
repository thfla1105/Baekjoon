import sys
input=sys.stdin.readline

n,m=map(int,input().split())
r,c,d=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,0,1,0] #북동남서
dy=[0,1,0,-1]

def turn_left(): 
    global d
    d = (d-1) % 4
 
count = 1
x, y = r, c
board[x][y] = 2 
 
while True:
    check = False 
    for i in range(4): 
        turn_left()
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < m: 
            if board[nx][ny] == 0:
                count += 1
                board[nx][ny] = 2 
                x, y = nx, ny
                check = True
                break
    if not check: 
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 2: 
                x, y = nx, ny
            elif board[nx][ny] == 1: 
                print(count)
                break
        else:
            print(count)
            break
    
