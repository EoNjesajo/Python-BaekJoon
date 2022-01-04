from collections import deque

T = int(input())
for _ in range(T):
  N,K = map(int,input().split()) 
  D = [0]+list(map(int,input().split()))
  node = [[] for _ in range(N+1)]
  q=deque()
  degree = [0]*(N+1)
  result = [0]*(N+1)
  for _ in range(K):
    X, Y = map(int,input().split())
    node[X].append(Y)
    degree[Y]+=1
  for i in range(1,N+1):
    if degree[i]==0:
      q.append(i);
      result[i] = D[i]

  while q:
    cur = q.popleft()
    for i in range(0,len(node[cur])):
      next = node[cur][i]
      degree[next]-=1
      result[next] = max(result[next],result[cur]+D[next])
      if degree[next]==0:
        q.append(next)
  W=int(input())
  print(result[W])

