from ..models import DATA

class DataDto(object):
    data_id: int

    def __init__(self, name: str, phone_number: str, email: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email
