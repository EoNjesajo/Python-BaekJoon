def turretFuntion(x1, y1, r1, x2, y2, r2):
  d = (x2-x1)**2 + (y2-y1)**2
  if x1==x2 and y1==y2 and r1==r2:
    return -1
  elif d>(r2+r1)**2 or d<(r2-r1)**2 :
    return 0
  elif d==(r2+r1)**2 or d==(r2-r1)**2 :
    return 1
  else :
    return 2


T=int(input())
for i in range(0,T):
  x1, y1, r1, x2, y2, r2 = input().split();
  print(turretFuntion(int(x1),int(y1),int(r1),int(x2),int(y2),int(r2)))
