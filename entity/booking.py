from datetime import datetime

class Booking:
    # Static booking_id counter to automatically increment for each booking
    booking_counter = 1

    def __init__(self, customer, event, num_tickets):
        self.booking_id = Booking.booking_counter
        Booking.booking_counter += 1  # Increment booking ID for each new booking
        self.customer = customer
        self.event = event
        self.num_tickets = num_tickets
        self.total_cost = self.calculate_booking_cost()
        self.booking_date = datetime.now()

    # Getter and Setter Methods
    def get_booking_id(self):
        return self.booking_id

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_event(self):
        return self.event

    def set_event(self, event):
        self.event = event

    def get_num_tickets(self):
        return self.num_tickets

    def set_num_tickets(self, num_tickets):
        self.num_tickets = num_tickets
        self.total_cost = self.calculate_booking_cost()  # Recalculate total cost after changing the number of tickets

    def get_total_cost(self):
        return self.total_cost

    def get_booking_date(self):
        return self.booking_date
    
    # Method to calculate the total cost of the booking
    def calculate_booking_cost(self):
        return self.num_tickets * self.event.ticket_price

    # Method to display booking details
    def display_booking_details(self):
        print(f"Booking ID: {self.booking_id}")
        print(f"Customer: {self.customer.customer_name}")
        print(f"Event: {self.event.event_name}")
        print(f"Number of Tickets: {self.num_tickets}")
        print(f"Total Cost: {self.total_cost}")
        print(f"Booking Date: {self.booking_date}")


    # Additional method to cancel a booking
    def cancel_booking(self):
        # Update the available seats in the event when the booking is canceled
        self.event.available_seats += self.num_tickets
        print(f"Booking {self.booking_id} has been canceled. {self.num_tickets} tickets refunded.")
