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
        return ("%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s, "
                "%s"
                %
                (self.id,
                 self.name,
                 self.brewery_type,
                 self.address_1,
                 self.address_2,
                 self.address_3,
                 self.city,
                 self.state_province,
                 self.postal_code,
                 self.country,
                 self.longitude,
                 self.latitude,
                 self.phone,
                 self.website_url,
                 self.state,
                 self.street))
