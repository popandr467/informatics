print(('NO','YES')[(lambda x,y:all((x**2+y**2>4,x<2,y<x)))(*map(float,input().split()))])