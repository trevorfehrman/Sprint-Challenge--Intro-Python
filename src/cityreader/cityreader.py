import csv


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = float(lat)
        self.lon = float(lon)


cities = []


def cityreader(cities):
    with open('cities.csv') as csvfile:
        parsed_data = csv.reader(csvfile)
        next(parsed_data)
        for record in parsed_data:
            cities.append(City(record[0], record[3], record[4]))
    return cities


cityreader(cities)

# # Print the list of cities (name, lat, lon), 1 record per line.
for city in cities:
    print(city.name, city.lat, city.lon)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

coords_alpha = input("Gimme: lat, lon: ").split(",")

coords_beta = input("Gimme: lat, lon again: ").split(",")

coords_alpha[0] = int(coords_alpha[0])
coords_alpha[1] = int(coords_alpha[1])

coords_beta[0] = int(coords_beta[0])
coords_beta[1] = int(coords_beta[1])

small_lat = None
big_lat = None
small_lon = None
big_lon = None

if coords_alpha[0] < coords_beta[0]:
    small_lat = coords_alpha[0]
    big_lat = coords_beta[0]
else:
    small_lat = coords_beta[0]
    big_lat = coords_alpha[0]

if coords_alpha[1] < coords_beta[1]:
    small_lon = coords_alpha[1]
    big_lon = coords_beta[1]
else:
    small_lon = coords_beta[1]
    big_lon = coords_alpha[1]

print(small_lat, big_lat, small_lon, big_lon)


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    # for city in cities:
    #   if city.lat >= small_lat and city.lat <= big_lat:

    within = [city.name for city in cities if city.lat >= lat1 and city.lat <=
              lat2 and city.lon >= lon1 and city.lon <= lon2]

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.
    print(within)
    return within


cityreader_stretch(small_lat, small_lon, big_lat, big_lon, cities)
