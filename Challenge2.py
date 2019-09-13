a={}
e=0
n=0
claim=[]
from datetime import date
with open("input3.txt") as k:
    for test in k:
        if e >=2:
            abc=test.split()
            claim.append(abc[6])
        e+=1


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
            claim_count =splitline[6]
            user=[nricfin , first_name, middle_name, last_name, date_of_birth, premium, claim_count]
            my_max = max(claim)
            if birthcalcu < 26 and user[6]< my_max:
                premium*=2
            if user[6] == my_max:
                premium*=3




            #endregion premium

            print(nricfin , first_name, middle_name, last_name, date_of_birth, premium)
        n+=1
