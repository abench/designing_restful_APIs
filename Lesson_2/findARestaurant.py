from geocode import getGeocodeLocation, getGeocodeLocationRequest
import json
import requests
import httplib2

from conspiratorial.designing_restful_APIs.api_keys import foursquare_client_id, foursquare_client_secret


import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

def findARestaurant(mealType, location):

    (latitude, longitude) = getGeocodeLocationRequest(location)

    url = 'https://api.foursquare.com/v2/venues/search'

    params = dict(
      client_id=foursquare_client_id,
      client_secret=foursquare_client_secret,
      v='20180323',
      ll='{},{}'.format(latitude,longitude),
      query=mealType,
      limit=1
    )
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    #print(data)
    result={}
    #name = ""

    #result['address'] = ""
    result['address'] = data['response']['venues'][0]['location']['address']

    #result['address'] = [name.append(i) for i in data['response']['venues'][0]['location']['formattedAddress']]
    return dict(
        name=data['response']['venues'][0]['name'],
        address=data['response']['venues'][0]['location']['address']
    )

# 1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.

# 2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
# HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

# 3. Grab the first restaurant
# 4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
# 5. Grab the first image
# 6. If no image is available, insert default a image url
# 7. Return a dictionary containing the restaurant name, address, and image url


if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    findARestaurant("Tacos", "Jakarta, Indonesia")
    findARestaurant("Tapas", "Maputo, Mozambique")
    findARestaurant("Falafel", "Cairo, Egypt")
    findARestaurant("Spaghetti", "New Delhi, India")
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    findARestaurant("Sushi", "Los Angeles, California")
    findARestaurant("Steak", "La Paz, Bolivia")
    findARestaurant("Gyros", "Sydney, Australia")