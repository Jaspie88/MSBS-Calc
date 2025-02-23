# ENTER DETAILS HERE
from datetime import date, timedelta

dob = date(1988,7,29)
join_date = date(2010,4,20)
now = date.today()
#years_of_service = timedelta(years= now - join_date)

years_of_service = 8
#final average salary
FAS = 175000
productivity = 200000


EBM = {
    1: 1 * 0.18,
    2: 2 * 0.18,
    3: 3 * 0.18,
    4: 4 * 0.18,
    5: 5 * 0.18,
    6: 6 * 0.18,
    7: 7 * 0.18,
    8: (7 * 0.18) + (1 * 0.23),
    9: (7 * 0.18) + (2 * 0.23),
    10: (7 * 0.18) + (3 * 0.23),
    11: (7 * 0.18) + (4 * 0.23),
    12: (7 * 0.18) + (5 * 0.23),
    13: (7 * 0.18) + (6 * 0.23),
    14: (7 * 0.18) + (7 * 0.23),
    15: (7 * 0.18) + (8 * 0.23),
    16: (7 * 0.18) + (9 * 0.23),
    17: (7 * 0.18) + (10 * 0.23),
    18: (7 * 0.18) + (11 * 0.23),
    19: (7 * 0.18) + (12 * 0.23),
    20: (7 * 0.18) + (13 * 0.23),
    21: (7 * 0.18) + (13 * 0.23) + (1 * 0.28),
    22: (7 * 0.18) + (13 * 0.23) + (2 * 0.28),
    23: (7 * 0.18) + (13 * 0.23) + (3 * 0.28),
    24: (7 * 0.18) + (13 * 0.23) + (4 * 0.28),
    25: (7 * 0.18) + (13 * 0.23) + (5 * 0.28),
    26: (7 * 0.18) + (13 * 0.23) + (6 * 0.28),
    27: (7 * 0.18) + (13 * 0.23) + (7 * 0.28),
    28: (7 * 0.18) + (13 * 0.23) + (8 * 0.28),
    29: (7 * 0.18) + (13 * 0.23) + (9 * 0.28),
    30: (7 * 0.18) + (13 * 0.23) + (10 * 0.28),    
    31: (7 * 0.18) + (13 * 0.23) + (11 * 0.28),
    32: (7 * 0.18) + (13 * 0.23) + (12 * 0.28),
    33: (7 * 0.18) + (13 * 0.23) + (13 * 0.28),
    34: (7 * 0.18) + (13 * 0.23) + (14 * 0.28),
    35: (7 * 0.18) + (13 * 0.23) + (15 * 0.28),
    36: (7 * 0.18) + (13 * 0.23) + (16 * 0.28),
    37: (7 * 0.18) + (13 * 0.23) + (17 * 0.28),
    38: (7 * 0.18) + (13 * 0.23) + (18 * 0.28),
    39: (7 * 0.18) + (13 * 0.23) + (19 * 0.28),
    40: (7 * 0.18) + (13 * 0.23) + (20 * 0.28)
}

# CALCULATIONS
EBM_total = EBM[years_of_service]
EB = FAS * EBM_total


fiftyfive_pension = round((EB / 12), 2)
sixty_pension = round((EB / 11), 2)
lumpsum = productivity

print("======================================")
print("===========--Your Results--===========")
print("Years of Service: ", years_of_service)
print("Employer Benifit Muiliplier: ", EBM_total)
print("Final Average Salary: $", FAS)
print("Employer Benifit Total: $", EB)
print("Lumpsum: $", productivity)
print("Pension at age 55: $", fiftyfive_pension)
print("Pension at age 60: $", sixty_pension)
print("======================================")
print("======================================")