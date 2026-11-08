import library as lib


class Book:
    name: str       # ksiazka musi miec nazwe!
    library: lib.Library
    publication_date: str
    author_name: str
    author_surname: str
    number_of_pages: int

    def __init__(self, name: str,
                 library: lib.Library,
                 date: str,
                 aname: str,
                 surname: str,
                 pages: int):
        self.name = name
        self.library = library
        self.publication_date = date
        self.author_name = aname
        self.author_surname = surname
        self.number_of_pages = pages

    def __str__(self):
        ret = (f'Ksiazka {self.name} '
               f'autorstwa {self.author_name} {self.author_surname}, '
               f'wydana w dniu {self.publication_date}. '
               f'Posiada az {self.number_of_pages} stron. '
               f'O bibliotece: ') + self.library.__str__()
        return ret
