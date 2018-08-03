t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    s = input()
    p = 0
    for j in range(0,n-k+1):
       for x in range(k):
           if s[j+x] != s[[j+x+1]:
                          p = p+1
    print(p)
