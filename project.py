import requests
import sys
from tabulate import tabulate


def main():
    #check command-line arguments
    args = check_cla(sys.argv[1:])
    #get weather data via API
    data = get_data(args)
    #calculate the distance between each emoji
    space = get_space(data)
    #plug space with emoji
    emoji = get_emoji(space)
    #print emoji
    print(*emoji)
    #print table
    print(tabulate(data, headers="firstrow",tablefmt="rounded_grid"))


def get_data(args):
    # set up API credentials
    api_key = "110f7719f281d328736c40d988dbda59"
    # build the API URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    #list of weather data list of each city, the first list is the header for the table
    cities = [["City","Weather","Temperature","Humidity","Wind Speed","Visibility", "Country"]]
    for city in args:
        # set the parameters for the API request
        params = {
            "q": city,
            "units": "imperial",
            "appid": api_key,
        }
        #request for data via API
        response1 = requests.get(url, params=params)
        if response1.status_code != 200:
            sys.exit(
                f'Invalid city "{city}", please try again.\nFor example: "New York"'
                     )
        #convert the output into json
        weather_data = response1.json()
        #parse the json data
        weather = weather_data["weather"][0]["description"]
        temp = weather_data["main"]["temp"]
        hum = weather_data["main"]["humidity"]
        ws = weather_data["wind"]["speed"]
        v = weather_data["visibility"]
        country = weather_data["sys"]["country"]
        #put all data of a city in a list, in order to pass it to the process funtion
        raw_list = [city, weather, temp, hum, ws, v, country]
        processed_list = process(raw_list)
        #append new list for each city
        cities.append(processed_list)
    #return the list of list
    return cities


def process(list):
    #get a list then round item, convert unit, append unit and return back a converted list\
    #convert °F into °C
    list[2] = round(((list[2] - 32) * (5/9)))
    #convert mph to m/s
    list[4] = round(list[4] * 0.44704)
    #convert m to km
    list[5] = round(list[5] / 1000)
    #process units
    list[0] = list[0].title()
    list[2] = f"{list[2]}°C"
    list[3] = f"{list[3]}%"
    list[4] = f"{list[4]}m/s"
    list[5] = f"{list[5]}km"
    return list


def check_cla(args):
    if len(args) < 1:
        sys.exit("Missing command-line argument\nWhich cities do you want to check?")
    #conver the list of cities into a set, in order to remove identical cities
    else:
        return set(args)


def get_space(data):
    #calculate space bettwen each emoji, based on the length of strings
    #creat a default list of spaces, except the first twos
    space = [0, 0, 5, 10, 4, 4, 7]
    #calculate the fist twos
    for i in range(2):
        l = 0
        #loop through the list but skip the header
        for list in data[1:]:
            #calculate total letter of each city or weather
            l += len(list[i])
        #average
        l /= (len(data)-1)
        #devided by two to get in the middle of the column
        space[i] = round((l+2)/2)
    #concatenate with space
    for i in range(len(space)):
            space[i] *= " "
    return space


def get_emoji(space):
    #organize emojies with spaces
    emoji = ["🏙️", "🔆", "🌡️", "💧", "🍃", "👀", "🌏"]
    for i in range(len(emoji)):
        emoji[i] = space[i] + emoji[i] + space[i]
    return emoji


if __name__ == "__main__":
    main()