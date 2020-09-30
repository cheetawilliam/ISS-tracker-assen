#Created 29-09-2020

#import libraries
import urllib3
import json
from datetime import datetime
import turtle
import time
from dateutil import tz

#Initialize urllib3
http = urllib3.PoolManager()

def retrieve_data(link):
    #Get data from API
    req = http.request("GET", link)
    obj = json.loads(req.data.decode("utf-8"))
    return obj

def people_on_iss():
    """Display who is on the ISS."""
    link = "http://api.open-notify.org/astros.json"
    #Get people data from API
    obj = retrieve_data(link)

    #print who is on the ISS
    for i in range(len(obj["people"])):
        if obj["people"][i]["craft"] == "ISS":
            print(obj["people"][i]["name"])

def next_local_passes():
    """Display the next few passes of the ISS over coordinates given by user."""
    #Get location from user.
    print ("Please enter the coordinates to you location.")
    local_lon = input("longitutde: ")
    local_lat = input("latitude: ")
    
    #Get next few passes over user location from API
    link = ("http://api.open-notify.org/iss-pass.json?lat=" + local_lat + 
        "&lon=" + local_lon)
    obj = retrieve_data(link)
    
    #Display each pass one by one.
    for i in range(len(obj["response"])):
        #Display how many seconds ISS wil be above horizon.
        print (obj["response"][i]["duration"])
        #Convert UTS time into local device time.
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        utc = datetime.fromtimestamp(obj["response"][i]["risetime"])
        utc = utc.replace(tzinfo = from_zone)
        local=utc.astimezone(to_zone)
        #Print the time the ISS rises above the horizon.
        print (local)
        
def show_current_location():
    """Show where the ISS is located above the planet right now."""
    #Display a world map and set cooridnates linked to pixels
    while True:
        screen = turtle.Screen()
        screen.setup(1024, 515)
        screen.setworldcoordinates(-180, -90, 180, 90)
        screen.bgpic("worldmap.png")
        
        #Create an image of the ISS and place it.
        turtle.addshape("ISS.gif")
        iss= turtle.Turtle()
        iss.shape("ISS.gif")
        iss.setheading(98)
        
        #Get current position of the ISS
        while True:
            link = "http://api.open-notify.org/iss-now.json"
            #Get current location data from API
            obj = retrieve_data(link)
            lat = float(obj["iss_position"]['latitude'])
            lon = float(obj['iss_position']["longitude"])
            #Move the ISS to current position.          
            iss.penup()
            iss.goto(lon, lat)
            #Wait 10 seconds.
            time.sleep(10)
        
        turle.done()

def start_program():
    """Start program and ask what someone wants to know about the ISS."""
    print("Welcome to ISS tracker, what would you like to know? type:\n"
        "A Who is on the ISS.\nB When does the ISS pass over you next.\n"
        "C Where above earth is the ISS now.")
    choice = input().lower()
    if choice == "a":
        people_on_iss()
    if choice == "b":
        next_local_passes()
    if choice == "c":
        show_current_location()

start_program()
