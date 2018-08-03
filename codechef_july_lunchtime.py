t= int(input())
for i in range(t):
    a,b,c,x,y=map(int,input().split())
    if a+b+c == x+y:
        if x-a>=0 and y-b>=0:
            if c == (x-a)+(y-b):
                print('YES')
            else:
                print('NO')
        elif x-a>=0 and y-c>=0:
            if b == (x-a)+(y-c):
                print('YES')
            else:
                print('NO')
        elif x-c>=0 and y-b>=0:
            if a == (x-c)+(y-b):
                print('YES')
            else:
                print('NO')
        elif x-c>=0 and y-a>=0:
            if b == (x-c)+(y-a):
                print('YES')
            else:
                print('NO')
        elif x-b>=0 and y-a>=0:
            if c == (x-b)+(y-a):
                print('YES')
            else:
                print('NO')
        elif x-b>=0 and y-c>=0:
            if a == (x-b)+(y-c):
                print('YES')
            else:
                print('NO')
        else:
            print('NO')

    else:
        print('NO')
