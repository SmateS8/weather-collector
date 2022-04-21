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
edit_line = 0
cached_file = []
#adds the latitude and longitude to the base url
url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + str(api_key)
print("Api URL will be : " + url)
#Gets date and time and formats it
now = datetime.datetime.now()
date = now.strftime("%d.%m")
time = now.strftime("%H" )
print("Date and time is : " + date + " " + time + " hours")
#FOR TESTING TIME IS PERMANENTLY SET BY LINE BELOW!
time = 6
def K_to_C(K):
    C = K - 273.15
    C = round(C,2)
    return C
#prints CSV file and finds line with right date
with open("data.csv", "r") as file:
    reader = csv.reader(file) 
    for line in reader:
        edit_line = edit_line + 1
        if line[0] == date:
            print("Date is the same")
            break
# cache the file into list            
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        cached_file.append(line)
print(cached_file[edit_line - 1])
#Checks if it is right time and gets data from API.
if int(time)== 6 or int(time) == 12 or int(time) == 18:
    resp = get(url)
    api_data = resp.json()
    if resp.status_code == 200:
       print("Communication with weather api was successful!")
    else:
        print("Something went wrong!")
        print ("Check the error code "+ str(resp))
