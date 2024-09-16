from datetime import date

#-------- ENTER DETAILS HERE --------#
dob = date(1988,7,29)
join_date = date(2010,4,20)
final_average_salary = 120000
planned_discharge_age = 41
estimated_future_salary = 160000
#------------------------------------#

# Functions to calculate service years and EBM
def age_at_date(dob, target_date):
    return target_date.year - dob.year - ((target_date.month, target_date.day) < (dob.month, dob.day))

def service_years_till_age(dob, join_date, target_age):
    target_date = date(dob.year + target_age, dob.month, dob.day)
    return age_at_date(join_date, target_date)

def years_of_service_prorated(join_date, end_date):
    delta = end_date - join_date
    years = delta.days / 365.25
    return years

def calculate_EBM(years_of_service):
    if years_of_service <= 7:
        return years_of_service * 0.18
    elif years_of_service <= 20:
        return (7 * 0.18) + ((years_of_service - 7) * 0.23)
    else:
        return (7 * 0.18) + (13 * 0.23) + ((years_of_service - 20) * 0.28)

now = date.today()
current_age = age_at_date(dob, now)
planned_discharge_date = date(dob.year + planned_discharge_age, dob.month, dob.day)
years_future = years_of_service_prorated(join_date, planned_discharge_date)
EBM_future = round(calculate_EBM(years_future), 2)
EB_future = estimated_future_salary * EBM_future
fiftyfive_pension_future = round((EB_future / 12), 2)
sixty_pension_future = round((EB_future / 11), 2)
years = years_of_service_prorated(join_date, now)
EBM_total = round(calculate_EBM(years), 2)
EB = final_average_salary * EBM_total
fiftyfive_pension = round((EB / 12), 2)
sixty_pension = round((EB / 11), 2)

# Display results
print("======================================")
print("======================================")
print("--------------------------------------")
print("----------  Discharge today  ---------")
print("--------------------------------------")
print(f"Years of Service (prorated): {years:.2f}")
print("Employer Benefit Multiplier: ", EBM_total)
print("Final Average Salary: $", final_average_salary)
print("Employer Benefit Total: $", round(EB, 2))
print("Pension at age 55: $", fiftyfive_pension)
print("Pension at age 60: $", sixty_pension)
print("--------------------------------------")
print(f"---------  Discharge at {planned_discharge_age}  ----------")
print("--------------------------------------")
print(f"Years of Service (prorated): {years_future:.2f}")
print("Employer Benefit Multiplier: ", EBM_future)
print("Estimated Future Salary: $", estimated_future_salary)
print("Employer Benefit Total: $", round(EB_future, 2))
print("Pension at age 55: $", fiftyfive_pension_future)
print("Pension at age 60: $", sixty_pension_future)
print("--------------------------------------")
print("======================================")
print("======================================")
