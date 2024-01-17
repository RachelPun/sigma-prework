import datetime as DT


def date_val():
    while True:
        try:
            date = DT.datetime.strptime(
                input("Please enter a date as yyyy/mm/dd"), "%Y/%m/%d")
            break
        except:
            print("Not a valid date. Please try again")
    return date


date = date_val()
today = DT.date.today()


def age_cal():
    years = today.year - date.year
    if today.month < date.month:
        years -= 1
    elif today.month == date.month:
        if today.day < date.day:
            years -= 1
    return years


print(age_cal())
