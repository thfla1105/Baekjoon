from itertools import combinations

n=int(input())
ability=[list(map(int,input().split())) for _ in range(n)]

member=[i for i in range(n)]
min_val=1e9

for t1 in combinations(member,n//2):
  start,link=0,0
  t2=list(set(member)-set(t1)) #상대팀

  for c in combinations(t1,2):
    start+=ability[c[0]][c[1]]
    start+=ability[c[1]][c[0]]
  
  for c in combinations(t2,2):
    link+=ability[c[0]][c[1]]
    link+=ability[c[1]][c[0]]
  
  min_val=min(min_val,abs(start-link))

print(min_val)