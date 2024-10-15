from entity.event import Event

class Concert(Event):
    def __init__(self, event_name, event_date, event_time, venue, total_seats, available_seats, ticket_price, artist, concert_type):
        super().__init__(event_name, event_date, event_time, venue, total_seats, available_seats, ticket_price, "Concert")
        self.artist = artist
        self.concert_type = concert_type

    # Getter and Setter Methods
    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_concert_type(self):
        return self.concert_type

    def set_concert_type(self, concert_type):
        self.concert_type = concert_type
    
    def display_event_details(self):
        super().display_event_details()
        print(f"Artist: {self.artist}, Concert Type: {self.concert_type}")

