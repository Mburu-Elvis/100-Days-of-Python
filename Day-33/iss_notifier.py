import requests
from datetime import datetime
import smtplib


my_lat = -0.240903
my_long = 35.717577

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_long = float(data['iss_position']['longitude'])

    if my_lat-5 <= iss_lat <= my_lat+5 and my_long-5 <= iss_long <= my_long+5:
        return True

def is_night():
    parameters = {
        'lat': my_lat,
        'lng': my_long,
        'formatted': 0,
    }
    response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msq='Subject: Look up\n\n ISS is above you in the sky'
    )