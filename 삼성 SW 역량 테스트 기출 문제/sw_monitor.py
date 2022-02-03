import copy
from itertools import combinations

n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
cctv=[]
for i in range(n):
  for j in range(m):
    k=board[i][j]
    if k!=0 and k!=6:
      cctv.append([k,i,j])
    
min_val=float('inf')
num=[i for i in range(1,5)]

def fill(dir,arr,i):
  if dir==1: #상
    for k in range(cctv[i][1]-1,0-1,-1):
      if arr[k][cctv[i][2]]==0:
        arr[k][cctv[i][2]]='#'
      elif arr[k][cctv[i][2]]==6:
        return arr
  if dir==2: #하
    for k in range(cctv[i][1]+1,n):
        if arr[k][cctv[i][2]]==0:
          arr[k][cctv[i][2]]='#'
          
        elif arr[k][cctv[i][2]]==6:
          
          return arr
  if dir==3: #좌
    for k in range(cctv[i][2]+1,m):
      if arr[cctv[i][1]][k]==0:
        arr[cctv[i][1]][k]='#'
        
      elif arr[cctv[i][1]][k]==6:
        
        return arr
  if dir==4:
    for k in range(cctv[i][2]-1,0-1,-1):
      if arr[cctv[i][1]][k]==0:
        arr[cctv[i][1]][k]='#'
        
      elif arr[cctv[i][1]][k]==6:
        
        return arr

  return arr

array=copy.deepcopy(board)
def solution(arr,i):
  global min_val,num
  tmp=0
  if i==len(cctv):
    for a in arr:
      tmp+=a.count(0)
    min_val=min(min_val,tmp)
  else:
    if cctv[i][0]==1:
      for j in range(1,5):
        solution(fill(j,copy.deepcopy(arr),i),i+1)
    if cctv[i][0]==2:
      for l in [[1,2],[3,4]]:
        arr1=copy.deepcopy(arr)
        for j in l:
          arr1=fill(j,arr1,i)
        solution(arr1,i+1)
    if cctv[i][0]==3:
      for l in [[1,3],[1,4],[2,3],[2,4]]:
        arr1=copy.deepcopy(arr)
        for j in l:
          arr1=fill(j,arr1,i)
        solution(arr1,i+1)
    if cctv[i][0]==4:
      for cb in list(combinations(num,3)):
        arr1=copy.deepcopy(arr)
        for c in cb:
          arr1=fill(c,arr1,i)
        solution(arr1,i+1)
    if cctv[i][0]==5:
      arr1=copy.deepcopy(arr)
      for j in range(1,5):
        arr1=fill(j,arr1,i)
      solution(arr1,i+1)

solution(array,0)
print(min_val)