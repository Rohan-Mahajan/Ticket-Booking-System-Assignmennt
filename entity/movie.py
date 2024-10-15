from entity.event import Event

class Movie(Event):
    def __init__(self, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, genre, actor_name, actress_name):
        super().__init__(event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, "movie")
        self.genre = genre
        self.actor_name = actor_name
        self.actress_name = actress_name

    def display_event_details(self):
        super().display_event_details()
        print(f"Genre: {self.genre}, Actor: {self.actor_name}, Actress: {self.actress_name}")

    # Getter and Setter Methods
    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_actor_name(self):
        return self.actor_name

    def set_actor_name(self, actor_name):
        self.actor_name = actor_name

    def get_actress_name(self):
        return self.actress_name

    def set_actress_name(self, actress_name):
        self.actress_name = actress_name
