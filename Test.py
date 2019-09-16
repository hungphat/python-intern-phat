from datetime import date
class User :
    def __init__(self, nricfin, first_name, middle_name, last_name, date_of_birth, premium, claim_count):
        self.nricfin  = nricfin
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.premium = premium
        self.claim_count = claim_count
        f


    def age(self):
        from datetime import date
        birthdaycalcu=today.year - bdyear - ((today.month, today.day) < (bdmonth, bdday))
        return birthdaycalcu
        pass

    def display(self):
        print()
        print(f'''{self.nricfin} {self.first_name} {self.middle_name} {self.last_name}
                    {self.age()} {self.date_of_birth} {self.premium}''')


class File:
    def __init__(self, filepath):
        self.lines = []
        self.users = []
        with open(filepath, 'r') as f:
            self.lines.append(f.readline())

    def create_user_list(self):
        for l in self.lines:
            self.users.append(self.parse_line(l))

    def birthday_parse(selfs):
        birthdayca = selfs.users[5].split('-')

    # def parse_line(self, line):
    #     id = "dfdfdf"
    #     name = "phat"
    #     birthday = '2019-08-12'
    #     return User(id, name, birthday)


file = File('input3.txt')
file.create_user_list()
print(file.users)