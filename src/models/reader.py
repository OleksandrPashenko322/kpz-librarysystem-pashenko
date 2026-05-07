# src/models/reader.py
class Reader:
    def __init__(self, name, email, library_card_number):
        self.name = name
        self.email = email
        self.library_card_number = library_card_number
        self.is_active = True