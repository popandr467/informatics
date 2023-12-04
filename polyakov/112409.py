print('\n'.join(f"{j+1}. {i}" for j,i in enumerate(sorted(i[i.index('.')+2:] for i in (input() for _ in range(int(input()))))))
