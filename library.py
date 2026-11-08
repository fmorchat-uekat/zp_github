class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str

    def __init__(self, city: str,
                 street: str,
                 zip: str,
                 hrs: str,
                 phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip
        self.open_hours = hrs
        self.phone = phone

    def __str__(self):
        return (f'Biblioteka w miescie {self.city}, '
                f'na ulicy {self.street}, kod pocztowy {self.zip_code}. '
                f'Otwarta w godzinach {self.open_hours}, '
                f'nr telefonu {self.phone}.')
