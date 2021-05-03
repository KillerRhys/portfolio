import requests as rq
from datetime import datetime as dt
import smtplib
import time

EMAIL = ''
PASSWORD = ''
MY_LAT = 39.554920
MY_LONG = -84.304610


def iss_overhead():
    response = rq.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    ISS = response.json()

    iss_lat = float(ISS['iss_position']['latitude'])
    iss_long = float(ISS['iss_position']['longitude'])

    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True


def night_walker():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'formatted': 0,
    }
    now = dt.now().hour
    timer = rq.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    timer.raise_for_status()
    data = timer.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    if now >= sunset or now <= sunrise:
        return True


while True:
    time.sleep(300)
    if iss_overhead() and night_walker():
        connection = smtplib.SMTP('smpt.gmail.com')
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject: Look up!\n\nThe space station is currently overhead!"
        )
