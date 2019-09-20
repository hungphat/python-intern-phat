class Customer:
    name = ''
    premium = 122.333

    def __str__(self):
        return f'{self.name} {self.premium}'

    def __repr__(self):
        return f'{self.name} {self.premium}'

c1 = Customer()
c1.name = 'abb'
c1.premium = 4.55

c_all = []
c_all.append(c1)

print(c_all)
for c in c_all:
    print(c)
