from entity.event import Event

class Sports(Event):
    def __init__(self, event_name, event_date, event_time, venue, total_seats, available_seats, ticket_price, sport_name, teams_name):
        super().__init__(event_name, event_date, event_time, venue, total_seats, available_seats, ticket_price, "Sports")
        self.sport_name = sport_name
        self.teams_name = teams_name

    # Getter and Setter Methods
    def get_sport_name(self):
        return self.sport_name

    def set_sport_name(self, sport_name):
        self.sport_name = sport_name

    def get_teams_name(self):
        return self.teams_name

    def set_teams_name(self, teams_name):
        self.teams_name = teams_name
    
    def display_event_details(self):
        super().display_event_details()
        print(f"Sport: {self.sport_name}, Teams: {self.teams_name}")

