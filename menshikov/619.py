d=tuple(tuple(map(int,input())) for i in range(int(input())))
m,n=len(d),len(d[0])
s=[[0]*n for i in range(m)]
s[0][0]=d[0][0]
for i in range(1,m):s[i][0]=d[i][0]+s[i-1][0]
for i in range(1,n):s[0][i]=d[0][i]+s[0][i-1]
for i in range(1,m):
	for j in range(1,n):s[i][j]=d[i][j]+min(s[i-1][j],s[i][j-1])
way=[[0]*n for i in range(m)]
i,j=m-1,n-1
while (i,j)!=(0,0):
	way[i][j]=1
	if i==0:
		for x in range(j,-1,-1):way[0][x]=1
		break
	elif j==0:
		for y in range(i,-1,-1):way[y][0]=1
		break
	else:
		if s[i-1][j]<s[i][j-1]:i-=1
		else:j-=1
print('\n'.join(''.join(map('-#'.__getitem__,i)) for i in way))