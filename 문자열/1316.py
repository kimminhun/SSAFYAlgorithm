#그룹단어체커
n = int(input())

cnt = n
for word in range(n):
    a = []
    wl= list(input())
    a.append(wl[0])
    for x in range(1, len(wl)):
        if wl[x] != a[-1]:
            a.append(wl[x])
    print(a)
    for s in a:
        if a.count(s) == 1:
            continue
        elif a.count(s) >=2:
            cnt -= 1
            break
print(cnt)


