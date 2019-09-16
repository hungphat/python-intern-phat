e=0
from datetime import date
# with open("input3.txt") as k:
#     for test in k:
#         if e >=2:
#             abc=test.split()
#             claim.append(abc[6])
#         e+=1
with open("input3.txt") as f:
    #next(f)
    for line in f:
        if e>0:
            print(line.rstrip())
        e+=1
