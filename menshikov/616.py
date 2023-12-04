x=sorted(map(int,input().split()))
def p(x):
    s=set(x)
    c=sorted(map(x.count,s))
    if len(s)==1:return 'Impossible'
    if c==[1,4]:return 'Four of a Kind'
    if c==[2,3]:return 'Full House'
    if {j-i for i,j in zip(x,x[1:])}=={1}:return "Straight"
    if c==[1,1,3]:return "Three of a Kind"
    if c==[1,2,2]:return "Two Pairs"
    if c==[1,1,1,2]:return "One Pair"
    return "Nothing"
print(p(x))