#from datetime import date
# class User :
#     def __init__(self, nricfin, first_name, middle_name, last_name, date_of_birth, premium, claim_count):
#         self.nricfin  = nricfin
#         self.first_name = first_name
#         self.middle_name = middle_name
#         self.last_name = last_name
#         self.date_of_birth = date_of_birth
#         self.premium = premium
#         self.claim_count = claim_count
#
#
#
#     def age(self):
#         from datetime import date
#         birthdaycalcu=today.year - bdyear - ((today.month, today.day) < (bdmonth, bdday))
#         return birthdaycalcu

#
#     def display(self):
    #
    #     print(f'''{self.nricfin} {self.first_name} {self.middle_name} {self.last_name}
    #                 {self.age()} {self.date_of_birth} {self.premium}''')


class File:
    def __init__(self, filepath):
        self.filepath = filepath
        self.lines = []
        self.users = []
        f=open(filepath,'r')
        n=0

        for l in f:
            self.lines=l.split()
            if n >=2:
        #         new_user = User(nricfin=self.lines[0], first_name=self.lines[1], middle_name=self.lines[2],
        #                    last_name=self.lines[3], date_of_birth=self.lines[4], premium=self.lines[5], claim_count=self.lines[6])
        #         print(f"User === {new_user.__dict__}")
        #         age = new_user.age()
                self.users=l.split()
                print(self.users)
        #         break
        #
            n+=1
        # user = User()
        # age = user.age()

    # def get_output(self):
    #     f = open(self.filepath,'r')
    #     # todo
    #
    #     return lines # list type
    # def create_user_list(self):
    #     lines = self.get_output()
    #     n = 0
    #     self.lines = []
    #     self.users = []
    #     f1 = f.readlines()
    #     for l in f1:
    #         self.lines = l.split()
    #         if n >=2:
    #             self.users=l.split()
    #         n+=1



    # def create_user_list(self):
    #     n=0
    #     self.lines = a
    #     print(a)


    # def birthday_parse(selfs):
    #     birthdayca = selfs.users[5].split('-')

    # def parse_line(self, line):
    #     id = "dfdfdf"
    #     name = "phat"
    #     birthday = '2019-08-12'
    #     return User(id, name, birthday)


file = File('input3.txt')
