f  = open('..//Input-Output//input.txt', 'r')
wr = open('..//Input-Output//output.txt', 'w')
for a in f:
    c = a.strip()
    try:
        int(c)
        e = int(c)
        if e % 2 != 0:
            wr.write('Weird \n')
        if e >= 2 and e <= 5 and e % 2 == 0:
            wr.write('Not Weird \n')
        if e >= 6 and e <= 20 and e % 2 == 0:
            wr.write('Weird \n')
        if e > 20 and e % 2 == 0:
            wr.write('Not Weird \n')
    except ValueError:
        wr.write('Chi xet so nguyen \n')




wr.close()

