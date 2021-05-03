import requests as rq
import smtplib

email = ''
password = ''

parameters = {
    'lat': 39.554920,
    'lon': -84.304611,
    'exclue': 'current,daily,minutely',
    'appid': "5d15de47fc9b057d0dd9d4892cf6a516",
}

weather = rq.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
weather.raise_for_status()
data = weather.json()

# Check if any id in next 12 hrs is < 700
raining = False
hours = data['hourly'][:12]
for hour in hours:
    weather_id = hour['weather'][0]['id']
    if int(weather_id) < 700:
        raining = True

if raining:
    connection = smtplib.SMTP('smtp.google.com')
    connection.starttls()
    connection.login(user=email, password=password)
    connection.send_message(
        from_addr=email,
        to_addrs=email,
        msg="Subject: Rain! \n\n Bring an umbrella today it's looking like rain!"
    )
