a,b=map(float,input().split())
b-=1e-3
from random import uniform as ri
print(*(f'{ri(a,b):.3f}' for i in range(5)))