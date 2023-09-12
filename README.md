# CLI WEATHER TABLE
#### Video Demo:  https://youtu.be/XL5Te4vazb4
#### Description:
This is a Python script that retrieves weather data for a list of cities using the OpenWeatherMap API and disphay the data in a table format using the tabulate library. The script also calculates the distance between each column header and places an emoji in the center of the space.

The get_data() function retrieves the weather data for each city using the OpenWeatherMap API. It builds the API URL, sets the necessary parameters for the API request, and makes the request using requests.get(). If the request is successful, it converts the response into a JSON object, parses the necessary weather data, and adds the resulting data to a list of cities.

The process() function takes a list of weather data for a city and converts the units, rounds the values, and appends the appropriate unit suffix to each value. It then returns the processed list of data.

The check_cla() function checks the command-line arguments and ensures that at least one city is provided. It also removes any duplicate cities in the list.

The get_space() function calculates the amount of space between each emoji in the emoji forecast based on the length of the city and weather strings. It returns a list of spaces that will be used to format the output.

The get_emoji() function concatenates the appropriate amount of space with each emoji in the forecast and returns a list of the resulting emojis.
#### Requirements
•'requests' library
•'tabulate' library
•'sys' library
#### Installation
1. Clone the repository or download the script.
2. Install the required librarie by running 'pip install tabulate' in the terminal.
#### Usage
1. In the terminal, navigate to the directory containing the script.
2. Run the script using 'python project.py <city1> <city2> ... <cityN>', where <city1> <city2> ... <cityN>' are the names of the cities you want to retrieve weather data for. You can pass as many cities as you want.
3. The script will retrieve weather data for each city and display it in a table format with column headers for city, weather, temperature, humidity, wind speed, visibility, and country.
4. The script will also place an emoji in the center of each column headee, base on the distance between of each header.
5. The temperature is displayed in Celsius, the wind speed in meters per second, and the visibility in kilometers