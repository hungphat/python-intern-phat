f = open('input.txt', 'r')
c = []
for b in f:
    c.append(float(b.strip()))



e = open('ouput.txt', 'w')
e.write(str(min(c)))
e.close()









