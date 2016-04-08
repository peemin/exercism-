'''
exercise leap
'''

def is_leap_year(year):
    leapYear = False
    if year%4 == 0:
        leapYear = True
        if year%100 == 0 and year%400!=0:
            leapYear = False
            
    return leapYear