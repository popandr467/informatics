from math import sqrt
ps=[]
n=int(input())
for i in range(2,int(sqrt(n))+1):
	while not(n%i):
		n//=i
		ps.append(i)
if n!=1:ps.append(n)
print('*'.join(map(str,ps)))