t = int(input())
for i in range(t):
    m,n = map(int,input().split())
    arr = []
    for i in range(m):
	l = input()
	l=[i for i in l]
	arr.append(l)
    s = input()
    for i in s:
	if i =='R':
	    for i in range(m):
	arr[i] = ['0']*arr[i].count('0')+['1']*arr[i].count('1')
	
	elif i =='L':
	    for i in range(4):
	arr[i] = ['1']*arr[i].count('1')+['0']*arr[i].count('0')
    print(arr)
