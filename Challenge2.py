a={}
n=0
from datetime import date
with open("input3.txt") as f:
    #next(f)
    for line in f:
        if n==0:                        # lay dong so 1 neu n = 0 do dem tu 0
            #a[n]= line.rstrip()
            print(line.rstrip())
        if n>=2:                        #lay tu dong so 3
            #print(line.rstrip())        #lay tung dong thanh tung mang

            splitline=line.split()      # tach tung phan tu sau space
                                        # (neu muon tach bang dk khac thi them dieu kien vao .split() vd .split('#')

            #print(splitline)

            #region ID + Name nricfin, first_name, middle_name, last_name
            nricfin = splitline[0]+ ','
            first_name = splitline[1].title()
            middle_name = splitline[2][0].upper() + '.'
            last_name = splitline[3].upper()

            #endregion ID + Name  nricfin, first_name, middle_name, last_name

            #region tinh tuoi date_of_birth
            birth=splitline[4].split('-') #cat chuoi ngay thang nam
            bdyear = int(birth[0])
            bdmonth = int(birth[1])
            bdday = int (birth[2])
            today=date.today()

            # print(birth)
            #print(today)

            birthcalcu = today.year - bdyear - ((today.month, today.day) < (bdmonth, bdday))
            date_of_birth = str(birthcalcu) + ','
            #endregion tinh tuoi date_of_birth

            #region premium

            premium = int(splitline[5])
            claim_count = int(splitline[6])
            if claim_count < 2 and birthcalcu < 26:
                premium=premium * 2
            if claim_count == 2 :
                premium = premium * 3

            #endregion premium

            print(nricfin , first_name, middle_name, last_name, date_of_birth, premium)
        n+=1