import datetime as DT


def date_val():
    while True:
        try:
            date = DT.datetime.strptime(
                input("Please enter a date as yyyy/mm/dd: "), "%Y/%m/%d")
            break
        except:
            print("Not a valid date. Please try again.")
    return date


def age_cal():
    age = today.year - date.year
    if today.month < date.month:
        age -= 1
    elif today.month == date.month:
        if today.day < date.day:
            age -= 1
    return age


date = date_val()
today = DT.date.today()

print(age_cal())
