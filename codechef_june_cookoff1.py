t = int(input())
for i in range(t):
    l,r = map(int,input().split())
    k = 0
    for i in range(l,r+1):
        m = str(i)
        if m[-1] == '2':
            k+=1
        elif m[-1] == '3':
            k+=1
        elif m[-1] == '9':
            k+=1
    print(k)
