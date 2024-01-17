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


dateN = date_val()
today = DT.date.today()


def age_cal(date):
    years = today.year - dateN.year
    if today.month < dateN.month:
        years -= 1
    elif today.month == dateN.month:
        if today.day < dateN.day:
            years -= 1
    return years


print(age_cal(dateN))
