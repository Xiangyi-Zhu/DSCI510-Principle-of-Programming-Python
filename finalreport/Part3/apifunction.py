import pandas as pd
import re
from opencage.geocoder import OpenCageGeocode
import sys


def geocode(address):
    api_key = 'bf363d6f4cd5460f8bb7e9d26be7d1f4'
    geocoder = OpenCageGeocode(api_key)
    result = geocoder.geocode(address,no_annotation = '1')
    lat = result[0]['geometry']['lat']
    lng = result[0]['geometry']['lng']
    return (lat,lng)

if __name__ =="__main__":
    if len(sys.argv) == 1:
        print(geocode('7124 Woodman Ave Unit 3, Van Nuys, CA 91405'))
else:
    print(f'...Importing module {__name__}...')
        
