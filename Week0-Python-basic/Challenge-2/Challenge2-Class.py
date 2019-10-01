a={}
e=0
n=0
claim=[]
customer=[]
Claim_list=[]
users_list=[]
from datetime import date
today=date.today()

class Customer:  #TODO Phat should name the class Customer

    def __init__(self, nricfin, first_name, middle_name, last_name, dob, premium, claim_count):
        self.nricfin        = nricfin
        self.first_name     = first_name
        self.middle_name    = middle_name
        self.last_name      = last_name
        self.dob            = dob
        self.premium        = premium
        self.claim_count    = claim_count

    #TODO Phat add 1-2 blank lines before function
    def getNricfin(self):
        return self.nricfin
    
    def getdob(self):
        return today.year - int(self.dob[0:4])
    
    def getFirstName(self):
        return self.first_name.capitalize()
    
    def getMiddleName(self):
        return self.middle_name[0]
    
    def getLastName(self):
        return  self.last_name
       
    def getPremium(self, claim_count, maxclaim):
        age=today.year - int(self.dob[0:4])     #TODO Phat write method to compute age and use here
        if  age< 26 and claim_count < max(maxclaim):
            return int(self.premium) * 2
        if max(maxclaim) == claim_count:
            return int(self.premium) * 3
        return self.premium

    def getClaimCount(self):
        return self.claim_count

with open("input.txt",'r') as f:
    for a in f:
        if e>= 2:
            info = a.split()
            user_info = Customer(*info)
            users_list.append(user_info)
        e+=1
    Claim_list = [maxClaim.claim_count for maxClaim in users_list]
    print(Claim_list)
wr = open('output.txt', 'w')
with open("input.txt", 'r') as f:
    #next(f)
    for line in f:
        if n==0:                        # lay dong so 1 neu n = 0 do dem tu 0
            #a[n]= line.rstrip()
            wr.write(f'{line.strip()}\n')
        if n>=2:                        #lay tu dong so 3
            #test = Customer( 'nricfin', 'first_name', 'middle_name', 'last_name', 'dob', 'premium', 'claim_count')
            #print(test.getdob())
            info = line.split()
            #print(info)
            user_info = Customer(*info)

            wr.write(f'{user_info.getNricfin()}, {user_info.getFirstName()} '
                     f'{user_info.getMiddleName().upper()}. '
                     f'{user_info.getLastName().upper()}, '
                     f'{user_info.getdob()} '
                     f'{user_info.getPremium(user_info.getClaimCount(),Claim_list)} \n')
        n+=1
wr.close()
