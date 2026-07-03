import requests
from datetime  import datetime
import smtplib
import time
myemail ="xayehe3822@icotz.com"
mypass ="12345678"
MY_LAT = 51.507351
MY_LOG = -0.127758

def is_iss_overhead():
    response = requests.get(url= "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data= response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LOG-5 <= Iss_longitude<= MY_LOG+5:
        return True
def is_night():
    parameters = {
            
            "lat": MY_LAT,
            "lng": MY_LOG,
            "formatted": 0,
        }

    response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int( data ["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    time_now = datetime.now().hour
    if time_now>= sunset or time_now<=sunrise:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(myemail, mypass)
        connection.sendmail(
            from_addr =myemail,
            to_addr= myemail,
            msg ="Subject:LookUp \n\n The ISS is above you in the sky."
        )