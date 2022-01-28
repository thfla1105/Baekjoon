n=int(input())
number=list(map(int,input().split()))
operation=list(map(int,input().split()))

max_val=-1e9
min_val=1e9

def dfs(i,tmp,add,sub,mul,div):
  global n, number,max_val,min_val
  if i==n:
    max_val=max(max_val,tmp)
    min_val=min(min_val,tmp)
  if add:
    dfs(i+1,tmp+number[i],add-1,sub,mul,div)
  if sub:
    dfs(i+1,tmp-number[i],add,sub-1,mul,div)
  if mul:
    dfs(i+1,tmp*number[i],add,sub,mul-1,div)
  if div:
    dfs(i+1,int(tmp/number[i]),add,sub,mul,div-1)
  
dfs(1,number[0],operation[0],operation[1],operation[2],operation[3])

print(max_val)
print(min_val)