"""
For example, if there were five employees with salaries last year were $90, $30, $100, $40, and $20,
and the target payroll this year is $210, then 60 is a suitable salary cap, since 60+30+60+40+20 = 210.

Design an algorithm for computing the salary cap, given existing salaries and the target payroll.
"""

# If we get the payroll in sorted order we calculate the total payroll if the cap is the current element 
# [20, 30, 40, 90, 100], T = 210
# If 20 is cap then - 100 would be the total payroll
# [100, 140, 170, 270, 280] Total payroll when each elment is considered as cap
# Since 210 lies between 170 and 270 the cap should lie between 40 - 90
# T = sum(A[0], A[1], .. A[i]) + (n - k)c - where i in (0, k-1)

# Time - O(nlogn)
def find_salary_cap(target_payroll, current_salaries):
    current_salaries.sort()
    unadjusted_salary_sum = 0.0
    for i, current_salary in enumerate(current_salaries):
        adjusted_people = len(current_salaries) - i
        adjusted_salary_sum = current_salary * adjusted_people
        if unadjusted_salary_sum + adjusted_salary_sum >= target_payroll:
            return (target_payroll - unadjusted_salary_sum) / adjusted_people
        unadjusted_salary_sum += current_salary
    return -1.0

