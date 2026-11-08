import json
import requests
import brewery as br


def get_breweries():
    brewery_list: list = []
    response = (requests.get
                ("https://api.openbrewerydb.org/v1/breweries?per_page=20"))
    if response.status_code == 200:
        data = response.json()
        for brewery in data:
            brew = br.Brewery()
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
