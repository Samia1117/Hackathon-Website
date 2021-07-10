from googleplaces import GooglePlaces, types, lang
import requests
import json

# generated api key from gooogle cloud platform(gcp)
API_key = "AIzaSyDpfIU78gDkH9ojIVo72EzdUf6rDxEIVSs"

# Use my API key for making api request calls
google_places= GooglePlaces(API_key)

# call the function nearby search with the parameters as longitude, latitude,
# radius and type of place which needs to be searched
# type can be HOSPITAL, CAFE, BAR, CASINO, etc
query_result = google_places.nearby_search(
lat_lng ={'lat': 28.4089, 'lng': 77.3178}, # Need to get client_lat_lng when they type in, this is a random one for demo
radius = 5000, types = [types.TYPE_HOSPITAL], sensor=True)

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