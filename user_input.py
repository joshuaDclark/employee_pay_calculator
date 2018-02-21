firstname = 'firstname'
lastname = 'lastname'

email = firstname + lastname + '@email.com'

field_of_experience = 'place field here'

years_employed = int(0)
weekly_salary = int(0)
SSN = int(123456789)


def employment_cal():
    if years_employed >= 2:
        print(weekly_salary * 1.5)
    else:
        print(None)

def employee_info():
    return(firstname + ' ' + lastname)
    return(field_of_experience)
    return(email)
    return(years_employed)
    return(weekly_salary)
    return(SSN)


employee_info()






