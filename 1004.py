class time:
    def __init__(s,d,h,m,sc):
        m+=sc//60;h+=m//60;d+=h//24
        sc%=60;m%=60;h%=24
        s.d,s.h,s.m,s.s=d,h,m,sc
    @classmethod
    def parse(cls,st):return cls(*[0,0,0,0,*map(int,st.split(':'))][-4:])
    def __repr__(s):return f'{s.h:0>2}:{s.m:0>2}:{s.s:0>2}'+(f'+{s.d} days' if s.d else '')
    def __add__(s,o):return time(s.d+o.d,s.h+o.h,s.m+o.m,s.s+o.s)
print(time.parse(input())+time.parse(input())
