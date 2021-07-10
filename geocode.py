import googlemaps
from datetime import datetime

gmaps = googlemaps.Client(key="AIzaSyDpfIU78gDkH9ojIVo72EzdUf6rDxEIVSs")

# Geocoding an address 1
geocode_result = gmaps.geocode('Duke University West Campus')
print(geocode_result)
print("=============================================")
print(geocode_result[0])
print("=============================================")
print(geocode_result[0]['address_components'])
print("=============================================")
print(geocode_result[0]['formatted_address'])   # Gives: Few Quadrangle, Durham, NC 27710, USA 
print("=============================================")

# Geocoding an address 2: (my current address, checking that it works)
geocode_result = gmaps.geocode('1315 Morreene Road, Durham, NC')
print(geocode_result)
print("=============================================")
print(geocode_result[0])
print("=============================================")
print(geocode_result[0]['address_components'])
print("=============================================")
print(geocode_result[0]['formatted_address'])
print("=============================================")


# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
#print(reverse_geocode_result)

# Works
# Latitude = 28.3921486
# Longitude = 77.31992890000001
# new_reverse_geocode_result = gmaps.reverse_geocode((Latitude, Longitude))
# print(new_reverse_geocode_result[10:20])

# Request directions via public transit
# now = datetime.now()
# directions_result = gmaps.directions("Sydney Town Hall",
#                                      "Parramatta, NSW",
#                                      mode="transit",
#                                      departure_time=now)
