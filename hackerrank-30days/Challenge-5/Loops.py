f  = open('..//Input-Output//input.txt', 'r')
wr = open('..//Input-Output//output.txt', 'w')
for a in f:
    c= a.strip()
    try:
        int(c)
        for i in range(int(c)):
            print(i**2)
    except ValueError:
        wr.write('Ko phai so nguyen')