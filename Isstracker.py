#Created 29-09-2020

#import libraries
import urllib3
import json
from datetime import datetime
import turtle

#Initialize urllib3
http = urllib3.PoolManager()
#Get data from API
req = http.request("GET", "http://api.open-notify.org/iss-now.json")
obj = json.loads(req.data.decode("utf-8"))

#Conver time and print
time = datetime.fromtimestamp(obj["timestamp"])
print(time)
print(obj["iss_position"]['latitude'], obj['iss_position']["longitude"])

#Assen longditude and lattitude.
lat = 52.992753
lon = 6.5642284

req = http.request("GET", "http://api.open-notify.org/iss-pass.json?lat="
    "52.992753&lon=6.5642284")
obj = json.loads(req.data.decode("utf-8"))

for i in range(len(obj["response"])):
    print (obj["response"][i]["duration"])
    print (datetime.fromtimestamp(obj["response"][i]["risetime"]))

while True:
    screen = turtle.Screen()
    screen.setup(1024, 515)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("worldmap.png")

    screen.register_shape("ISS.png")
    iss= turtle.Turtle()
    iss.shape("ISS.png")
    iss.setheading(98)
