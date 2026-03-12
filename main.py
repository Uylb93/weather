import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

OWM_Endpoint="https://api.openweathermap.org/data/2.5/forecast"
MY_LAT=26.203
MY_LONG=-98.230
params={
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
     "cnt": 4 }
response = requests.get(OWM_Endpoint, params=params)
weather_data=response.json()
weather_info=weather_data["list"]
will_it_rain=False
for i in range(4):
    weather_num=weather_info[i]["weather"][0]["id"]
    if weather_num < 700:
        will_it_rain=True
if will_it_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
        body='it will rain',
        to='whatsapp:+'
    )
    print(message.status)
