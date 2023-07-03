l=list(map(int,input().strip().split()))
maxx=l[0]
for i in l:
    if maxx<i:
        maxx=i
print(maxx)