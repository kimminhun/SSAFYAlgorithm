import sys
input = sys.stdin.readline

v, e = map(int, input().split())
vroot = [i for i in range(v+1)]
elist = []
for _ in range(e):
    elist.append(list(map(int, input().split())))

elist.sort(key= lambda x : x[2])

def find(x):
    if x != vroot[x]:
        vroot[x] = find(vroot[x])
    return vroot[x]
def union(a,b):
    a = find(a)
    b = find(b)
    if a< b:
        vroot[b] = a
    else:
        vroot[a] = b
    
answer = 0

for s, e, c in elist:
    if not find(s) == find(e):
        union(s,e)
        answer += c
print(answer)

