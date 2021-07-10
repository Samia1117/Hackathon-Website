# client location is a string such as: 'Duke University West Campus'
# find the geocoding - location in latitude, longitude (along with some other details)
# find locations of places near to this location using the client latitude, longitude values
import googlemaps
from datetime import datetime
from googleplaces import GooglePlaces, types, lang
import requests
import json

def find_nearby_hospitals(client_location):
    API_key = "AIzaSyDpfIU78gDkH9ojIVo72EzdUf6rDxEIVSs"
    gmaps = googlemaps.Client(key=API_key)
    
    # Geocoding client address string to latitude and longitude
    geocode_result = gmaps.geocode(client_location)
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    print("Latitude: ",  lat,  " Longitude: ", lng)
    print("=============================================")
    print("Formatted address: ", geocode_result[0]['formatted_address'])
    print("=============================================")
    
    # Use lat-long values to get nearby hospitals:
    google_places= GooglePlaces(API_key)
    query_result = google_places.nearby_search(lat_lng ={'lat': lat, 'lng': lng},
    radius = 500, types = [types.TYPE_HOSPITAL], sensor=True)
    
    # If any attributions related with search results print them
    if query_result.has_attributions:
        print (query_result.html_attributions)

    # Iterate over the search results
    for place in query_result.places:
        # print(type(place))
        # place.get_details()
        print (place.name)
        print("Latitude", place.geo_location['lat'])
        print("Longitude", place.geo_location['lng'])
        print()

client_location = '1315 Morreene Road, Durham Nc'
print("location: ", client_location)
find_nearby_hospitals(client_location)


#============= The search results seem perfect ======================
# location:  1315 Morreene Road, Durham Nc
# Latitude:  36.0047581  Longitude:  -78.95251150000001
# =============================================
# Formatted address:  1315 Morreene Rd, Durham, NC 27705, USA
# =============================================
# Duke Center For Living
# Latitude 36.0012967
# Longitude -78.95569069999999

# Lenox Baker Children's Hospital
# Latitude 36.0050735
# Longitude -78.9500214

# PruittHealth - Durham
# Latitude 36.0040319
# Longitude -78.95092609999999

# =================             ======================







# print("")
# client_location = 'Asian Institute of Medical Sciences'
# print("Next location: ", client_location)
# find_nearby_hospitals(client_location)

# print("")
# client_location = 'Metro Heart Institute with Multispeciality'
# print("Next location: ", client_location)
# find_nearby_hospitals(client_location)

# print("")
# client_location = 'Rawat Medical Store'
# print("Next location: ", client_location)
# find_nearby_hospitals(client_location)