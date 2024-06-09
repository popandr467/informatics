input()
s=input()
o,c='({[',')}]'
t=dict(zip(c,o))
o,c=set(o),set(c)
def r():
    st=[]
    for i in s:
        if i in o:st.append(i)
        else:
            if not st:return 0
            if st.pop()!=t[i]:return 0
    return not st
print(('No','Yes')[r()])