import requests
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

openweathermapkey = "3f2072d93520b12df53393a7c9e0b006"
# using email/username of yuvalco@yahoo.com
mylat = 31.979672
mylon = 34.770994



parameters = {
    "lat": mylat,
    "lon": mylon,
    "appid": openweathermapkey,
    "units": "metric",
    "cnt":4,
}

#https://opentdb.com/api.php?amount=10&type=boolean

data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?", params=parameters)
data.raise_for_status()
forecast = data.json()

#print(forecast)
response_code = forecast["cod"]
forecast_data = forecast["list"]
print(response_code)
print(forecast_data)
bring_umbrella = False
for i in range(len(forecast_data)):
    if int(forecast_data[i]["weather"][0]["id"]) < 700:
        bring_umbrella = True
        print("Bring an umbrella")
        break

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
print (os.environ['TW_AUTH_TOKEN'])


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC539006afe824de805e3cd12db79657cb'
auth_token = os.environ['TW_AUTH_TOKEN']
client = Client(account_sid, auth_token)
umbrella_message = "It is going to rain today, Take an umbrella"

if bring_umbrella:
    message = client.messages \
                    .create(
                         body=umbrella_message,
                         from_='+18286772715',
                         to='+972545555362'
                     )

    print(message.status)