import json
import requests

class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: str
    address_2: str
    address_3: str
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: float
    latitude: float
    phone: str
    website_url: str
    state: str
    street: str

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.name, self.brewery_type, self.address_1, self.address_2, self.address_3, self.city, self.state_province, self.postal_code, self.country, self.longitude, self.latitude, self.phone, self.website_url, self.state, self.street)

def get_breweries():
    brewery_list: list = []
    response = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=20")
    if response.status_code == 200:
        data = response.json()
        for brewery in data:
            brew = Brewery()
            brew.id = brewery.get("id")
            brew.name = brewery.get("name")
            brew.brewery_type = brewery.get("brewery_type")
            brew.address_1 = brewery.get("address_1")
            brew.address_2 = brewery.get("address_2")
            brew.address_3 = brewery.get("address_3")
            brew.city = brewery.get("city")
            brew.state_province = brewery.get("state_province")
            brew.postal_code = brewery.get("postal_code")
            brew.country = brewery.get("country")
            brew.longitude = brewery.get("longitude")
            brew.latitude = brewery.get("latitude")
            brew.phone = brewery.get("phone")
            brew.website_url = brewery.get("website_url")
            brew.state = brewery.get("state")
            brew.street = brewery.get("street")
            brewery_list.append(brew)
    for brewery in brewery_list:
        print(brewery.__str__())

get_breweries()