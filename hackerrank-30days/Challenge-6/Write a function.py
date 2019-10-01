f  = open('..//Input-Output//input.txt', 'r')
wr = open('..//Input-Output//output.txt', 'w')
d=[]

def is_year(year):
    try:
        int(year)
        if year %4 != 0 and year %100 ==0:
            return False
        if year == 400 or year %4 ==0:
            return True
    except ValueError:
        print('Sai nhap lieu')
year = int(f.readline())
print(is_year(year))