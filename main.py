# imports library for reading API
from requests import get

# imports library for reading CSV files
import csv

# import library for real date and time
import datetime

#imports sleep function from time library
from time import sleep

lon = 0  # replace with your longitude
lat = 0  # replace with your latitude
api_key = "ABCD00"  # replace with your API key
base_url = "https://api.openweathermap.org/data/2.5/weather?"
edit_line = 0
cached_file = []
# adds the latitude and longitude to the base url
url = base_url + "lat=" + str(lat) + "&lon=" + \
    str(lon) + "&appid=" + str(api_key)
print("Api URL will be : " + url)
# Gets date and time and formats it
now = datetime.datetime.now()
date = now.strftime("%d.%m")
time = now.strftime("%H")
print("Date and time is : " + date + " " + time + " hours")
# FOR TESTING, TIME IS PERMANENTLY SET BY LINE BELOW!



def K_to_C(K):
    C = K - 273.15
    C = round(C, 2)
    return C


while True:
    edit_line = 0
    changed = False
    cached_file = []
    # reads CSV file and finds line with right date
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            edit_line = edit_line + 1
            if line[0] == date:
                print("Found the right line!")
                break

    # cache the file into list
    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for line in reader:
            cached_file.append(line)

    # Checks if it is right time and gets data from API.
    if int(time) == 7 or int(time) == 14 or int(time) == 20:
        resp = get(url)
        api_data = resp.json()
        print(api_data)
        if resp.status_code == 200:
            print("Communication with weather api was successful!")
        else:
            print("Something went wrong!")
            print("Check the error code " + str(resp))

        # Checks which right time is it and writes data
        if int(time) == 7:
            # writes the Temp_7
            cached_file[edit_line - 1][1] = K_to_C(float(api_data["main"]["temp"]))
            # writes Wind_7
            cached_file[edit_line - 1][4] = api_data['wind']["speed"]
            # writes Press_7
            cached_file[edit_line - 1][9] = api_data['main']["pressure"]
            # writes Humidity_7
            cached_file[edit_line - 1][12] = api_data['main']["humidity"]
            changed = True
        elif int(time) == 14:
            # writes the Temp_14
            cached_file[edit_line - 1][2] = K_to_C(float(api_data["main"]["temp"]))
            # writes Wind_14
            cached_file[edit_line - 1][5] = api_data["wind"]["speed"]
            # writes Press_14
            cached_file[edit_line - 1][10] = api_data['main']["pressure"]
            # writes Humidity_14
            cached_file[edit_line - 1][13] = api_data['main']["humidity"]
            changed = True
        elif int(time) == 20:
            # writes the Temp_20
            cached_file[edit_line - 1][3] = K_to_C(float(api_data['main']['temp']))
            # writes Wind_20
            cached_file[edit_line - 1][6] = api_data['wind']['speed']
            # writes Press_20
            cached_file[edit_line - 1][11] = api_data['main']['pressure']
            # writes Humidity_20
            cached_file[edit_line - 1][14] = api_data['main']['humidity']
            changed = True
    else:
        print("Its not right time!")
        changed = False

    # writes data into CSV file, if something was changed
    if changed == True:
        with open("data.csv", "w", newline='') as file:
            # prints changed line
            print(str(cached_file[edit_line - 1]))
            writer = csv.writer(file)
            for line in cached_file:
                writer.writerow(line)
            print("Data was written!")
    else:
        print("Nothing was changed.")
    #waits for half an hour
    print("Waiting for half an hour, then it will check again.")
    sleep(1800)

