print((lambda m,d,ms:(ms[m-1]-d+sum(ms[m:]) if 0<m<13 and 0<d<=ms[m-1] else -1))(*map(int,input().split()),(31,28,31,30,31,30,31,31,30,31,30,31)))