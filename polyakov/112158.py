print(*(lambda *a:(j for i,j in zip(a,'ABC') if i==max(a)) if len(set(a))>1 else [0])(*map(int,input().split())))