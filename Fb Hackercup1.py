t = int(input())
for i in range(t):
    n,k,v = map(int,input().split())
    arr = []
    dic = [0]*n
    d = {}
    l = []
    for j in range(n):

        x = input()
        arr.append(x)
        
    if v<=k:
        
        for x in range(1,v+1):
            d[x] = []
            for y in range(k):
                p = dic.index(min(dic))
                d[x].append(arr[p])
                dic[p] = dic[p] + 1
    else:
        for x in range(1,k+1):
            d[x] = []
            for y in range(k):
                p = dic.index(min(dic))
                d[x].append(arr[p])
                dic[p] = dic[p] + 1

    z = v%k
    if z !=0:
        print(d[z])
    else:
        print(d[k])
            
