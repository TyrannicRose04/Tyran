import requests
import datetime

d = datetime.date(2023, 9, 1)
df = datetime.datetime.now()
while d.year != df.year or d.month != df.month or d.day != df.day:
    month = d.month
    day = d.day
    if month < 10:
        month = "0" + str(d.month)
    if day < 10:
        day = "0" + str(d.day)
    url = ('https://www.cbr-xml-daily.ru/archive/' + str(d.year) + '/' + str(month) + '/' + str(day) + '/daily_json.js')
    response = requests.get(url).json()

    d += datetime.timedelta(days=1)

    date = response['Date']
    USD = response['Valute']['USD']['Value']

    with open('outfile.csv', 'a') as f:
        f.write(date)
        f.write(", ")
        f.write(str(USD))
        f.write("\n")
