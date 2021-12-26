count0=[1,0]
count1=[0,1]

T = int(input())

for i in range(0,T):
  z = int(input())
  for j in range(2,41):
    count0.append(count0[j-1] + count0[j-2])
    count1.append(count1[j-1] + count1[j-2])
  print(count0[z],count1[z])

