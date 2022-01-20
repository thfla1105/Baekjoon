n=int(input())
schedule=[list(map(int,input().split())) for _ in range(n)]

work=[0]*(n+1)

for i in range(n-1,-1,-1):
  if i+schedule[i][0]>n:
    work[i]=work[i+1]
  else:
    work[i]=max(work[i+schedule[i][0]]+schedule[i][1],work[i+1])
print(work[0])