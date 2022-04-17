#imports library for reading API
from requests import get
#imports library for reading CSV files
import csv
#import library for real date and time
import datetime
lon = 0   #replace with your longitude
lat = 0   #replace with your latitude
api_key = "ABCD00"    #replace with your API key 
base_url = "https://api.openweathermap.org/data/2.5/weather?"
#adds the latitude and longitude to the base url
url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + str(api_key)
print("Api URL will be : " + url)
#Gets date and time and formats it
now = datetime.datetime.now()
date = now.strftime("%d.%m")
time = now.strftime("%H" )
print("Date and time is : " + date + "; " + time + " hours")
#prints CSV file and finds line with right date
with open("data.csv", "r") as file:
    reader = csv.reader(file) 
    for line in reader:
        print(line)
        if line[0] == date:
            print("Date is the same")

    