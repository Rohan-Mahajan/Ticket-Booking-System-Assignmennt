class Event:
    def __init__(self, event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type):
        self.event_name = event_name
        self.event_date = event_date  # This should be a date object
        self.event_time = event_time  # This should be a time object
        self.venue_id = venue_id
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.ticket_price = ticket_price
        self.event_type = event_type
    # Getter and Setter Methods
    def get_event_name(self):
        return self.event_name

    def set_event_name(self, event_name):
        self.event_name = event_name

    def get_event_date(self):
        return self.event_date

    def set_event_date(self, event_date):
        self.event_date = event_date

    def get_event_time(self):
        return self.event_time

    def set_event_time(self, event_time):
        self.event_time = event_time

    def get_venue(self):
        return self.venue

    def set_venue(self, venue):
        self.venue = venue

    def get_total_seats(self):
        return self.total_seats

    def set_total_seats(self, total_seats):
        self.total_seats = total_seats

    def get_available_seats(self):
        return self.available_seats

    def set_available_seats(self, available_seats):
        self.available_seats = available_seats

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price

    def get_event_type(self):
        return self.event_type

    def set_event_type(self, event_type):
        self.event_type = event_type

    
    def display_event_details(self):
        print(f"Event Name: {self.event_name}")
        print(f"Date: {self.event_date}, Time: {self.event_time}")
        print(f"Venue: {self.venue.venue_name}, Total Seats: {self.total_seats}, Available Seats: {self.available_seats}")
        print(f"Ticket Price: {self.ticket_price}, Event Type: {self.event_type}")

    def calculate_total_revenue(self):
        sold_tickets = self.total_seats - self.available_seats
        return sold_tickets * self.ticket_price

    def getBookedNoOfTickets(self):
        return self.total_seats - self.available_seats

    def book_tickets(self, num_tickets):
        if num_tickets > self.available_seats:
            print("Not enough tickets available!")
        else:
            self.available_seats -= num_tickets
            print(f"{num_tickets} tickets booked. {self.available_seats} remaining.")

    def cancel_booking(self, num_tickets):
        self.available_seats += num_tickets
        print(f"{num_tickets} tickets canceled. {self.available_seats} available.")