
def calculate(student,b,c):
  count=0
  for s in student:
    count+=1
    s=s-b
    if s<=0:
      continue
    else:
      if s%c!=0:
        count+=s//c+1
      else:
        count+=s//c
         
  return count

if __name__ == "__main__":
  n=int(input())
  student=list(map(int,input().split()))
  b,c=map(int,input().split())
  count= calculate(student,b,c)
  print(count)