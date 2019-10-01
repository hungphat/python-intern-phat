f  = open('..//Input-Output//input.txt', 'r')
wr = open('..//Input-Output//output.txt', 'w')
d = []
for a in f:
    c = a.strip()
    try:
        int(c)
        d.append(int(c))
    except ValueError:
        wr.write('Ko phai so nguyen')

count = len(d)
if count == 2:
    wr.write(f' {d[0] + d[1]} \n')
    wr.write(f' {d[0] - d[1]} \n')
    wr.write(f' {d[0] * d[1]} \n')
else:
    wr.write('Thieu hoac thua du lieu')
