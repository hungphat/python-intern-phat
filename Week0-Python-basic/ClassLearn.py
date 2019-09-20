from datetime import date
today=date.today()
class File:
    def __init__(self, nricfin, first_name, middle_name, last_name, date_of_birth, premium, claim_count):
        self.nricfin  = nricfin
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.premium = premium
        self.claim_count = claim_count

    def getFirst_name(self):
        return self.first_name.capitalize()





















#--------------Main------------------

a=File('input3.txt')
a.create_user_list()




