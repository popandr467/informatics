print('\n'.join((lambda a,b:[str(i) for i in range(a,b+1) if all(i%j for j in range(2,int(i**.5)+1))])(*map(int,input().split())) or ['Absent']))
