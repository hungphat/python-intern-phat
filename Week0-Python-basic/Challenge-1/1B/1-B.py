n = 0
f = open('input.txt', 'r')
c = []
d = []
for a in f:
    if n >=1:
        c.append(a.strip())
    n+=1
wr = open('output', 'w')

for e in c:
    t = max(c)
    if e == t:
        wr.write('1\n',t)
    else:
        wr.write('0 \n')
wr.close()


