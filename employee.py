class Employee:
    first_name: str
    last_name: str
    hire_date: str
    birth_date: str
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(self, name: str,
                 sname: str,
                 hdate: str,
                 bdate: str,
                 city: str,
                 street: str,
                 zip: str,
                 phone: str):
        self.first_name = name
        self.last_name = sname
        self.hire_date = hdate
        self.birth_date = bdate
        self.city = city
        self.street = street
        self.zip_code = zip
        self.phone = phone

    def __str__(self):
        return (f'{self.first_name}  {self.last_name}, '
                f'urodzony dnia {self.birth_date}. '
                f'Zatrudniony od dnia {self.hire_date}. '
                f'Zamieszkaly na ulicy {self.street} '
                f'w miescie {self.city} '
                f'(kod pocztowy {self.zip_code}), '
                f'nr telefonu: {self.phone}.')
