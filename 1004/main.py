T = int(input())
for i in range(0,T):
  count = 0
  x1,y1,x2,y2 = map(int,input().split()) 
  n = int(input())
  for n in range(0,n):
    cx, cy, r = map(int,input().split())
    result1 = True if pow(cx-x1,2)+pow(cy-y1,2)<pow(r,2) else False
    result2 = True if pow(cx-x2,2)+pow(cy-y2,2)<pow(r,2) else False
    if result1!=result2:
      count+=1
  print(count)



# x, y = map(int,input().split())
# print(x+y)