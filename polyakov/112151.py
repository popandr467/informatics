a,b=map(int,input().split())
from random import randint as ri
print(*(ri(a,b) for i in range(5)))