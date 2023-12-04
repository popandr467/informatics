def fill(mt,n,s,a):
    if s==n//2:
        if n&1:mt[s][s]=n**2
        return
    for i in range(s,n+~s):mt[s][i]=a+i
    for i in range(s,n+~s):mt[i][~s]=a+i+n-s*2-1
    for i in range(s,n+~s):mt[~s][~i]=a+i+(n-s*2-1)*2
    for i in range(s,n+~s):mt[~i][s]=a+i+(n-s*2-1)*3
    fill(mt,n,s+1,a+(n-s*2-1)*4-1)
mtx=(lambda n:[[0]*n for i in range(n)])(int(input()))
fill(mtx,len(mtx),0,1)
for i in mtx:print(*i,sep='\t')