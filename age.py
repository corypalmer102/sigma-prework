from datetime import datetime


def calc_age(date_string):
    # converting date_string into datetime object
    birth_date = datetime.strptime(date_string, "%d-%m-%Y")
    today = datetime.today()

    # calculating age
    age = today.year - birth_date.year

    # adjusting if birthday hasn't happened yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


print(calc_age("22-11-2003"))
print(calc_age("20-02-2004"))
