import httplib2
import json
import requests

from conspiratorial.designing_restful_APIs.api_keys import google_api_key

def getGeocodeLocation(inputString):
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY

    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)

def getGeocodeLocationRequest(inputString):

    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = dict(
        address=inputString.replace(" ", "+"),
        key=google_api_key
    )

    resp = requests.get(url=url,params=params)
    data = json.loads(resp.text)
    latitude = data['results'][0]['geometry']['location']['lat']
    longitude = data['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)


if __name__ == "__main__":
    print(getGeocodeLocation("Tokyo Japan"))
    print(getGeocodeLocationRequest("Tokyo Japan"))
    print(getGeocodeLocation("Jakarta Indonesia"))
    print(getGeocodeLocationRequest("Jakarta Indonesia"))
    print(getGeocodeLocation("Maputo Mozambique"))
    print(getGeocodeLocationRequest("Maputo Mozambique"))
    print(getGeocodeLocation("Cairo Egypt"))
    print(getGeocodeLocationRequest("Cairo Egypt"))
    print(getGeocodeLocation("New Delhi India"))
    print(getGeocodeLocationRequest("New Delhi India"))
    print(getGeocodeLocation("Geneva Switzerland"))
    print(getGeocodeLocationRequest("Geneva Switzerland"))
    print(getGeocodeLocation("Los Angeles California"))
    print(getGeocodeLocationRequest("Los Angeles California"))
    print(getGeocodeLocation("La Paz Bolivia"))
    print(getGeocodeLocationRequest("La Paz Bolivia"))
    print(getGeocodeLocation("Sydney Australia"))
    print(getGeocodeLocationRequest("Sydney Australia"))