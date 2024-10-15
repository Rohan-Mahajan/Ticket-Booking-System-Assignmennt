from util.db_connection import DBConnection
from exception.invalid_booking_id_exception import InvalidBookingIDException
from exception.event_not_found_exception import EventNotFoundException
from entity.booking import Booking

class BookingSystemServiceProviderImpl:
    def calculate_booking_cost(self, num_tickets, event):
        return num_tickets * event.ticket_price

    def book_tickets(self, event_name, customer_details, num_tickets):
        connection = DBConnection.getConnection()  # Get a new connection
        cursor = connection.cursor()

        # Insert new customer into the Customer table
        insert_customer_query = """
        insert into customer (customer_name, email, phone_number) 
        values (?, ?, ?);
        """
        cursor.execute(insert_customer_query, (customer_details['name'], customer_details['email'], customer_details['phone']))
        connection.commit()

        # Retrieve the last inserted customer_id
        cursor.execute("select scope_identity();")
        customer_id = cursor.fetchone()[0]  # Get the customer_id of the newly added customer

        # Fetch event details
        query = "select * from event where event_name = ?"
        cursor.execute(query, (event_name,))
        event = cursor.fetchone()

        if not event:
            raise EventNotFoundException(f"Event '{event_name}' not found.")

        available_seats = event[5]  # Index for available_seats in the query result
        if num_tickets > available_seats:
            print(f"Not enough tickets available for '{event_name}'")
            connection.close()  # Close connection if no booking is made
            return

        # Proceed with booking
        new_available_seats = available_seats - num_tickets
        update_query = "update event set available_seats = ? where event_name = ?"
        cursor.execute(update_query, (new_available_seats, event_name))

        # Insert into Booking table
        booking = Booking(customer_id, event, num_tickets)  # Use the new customer_id
        insert_query = """
        insert into booking (customer_id, event_id, num_tickets, total_cost, booking_date) 
        values (?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, (customer_id, event[0], num_tickets, booking.total_cost, booking.booking_date))

        connection.commit()
        connection.close()  # Close the connection after operations
        print(f"{num_tickets} tickets successfully booked for '{event_name}' for customer '{customer_details['name']}'")

        
    def cancel_booking(self, booking_id):
        connection = DBConnection.getConnection()  # Open a new connection
        cursor = connection.cursor()

        # Fetch booking details
        query = "select * from booking where booking_id = ?"
        cursor.execute(query, (booking_id,))
        booking = cursor.fetchone()

        if not booking:
            raise InvalidBookingIDException(f"Booking ID '{booking_id}' is invalid.")

        # Proceed with cancellation and updating available seats
        event_id = booking[2]  # Event ID in Booking table
        num_tickets = booking[3]  # Number of tickets in Booking table

        # Update event's available seats
        event_query = "select available_seats from event where event_id = ?"
        cursor.execute(event_query, (event_id,))
        available_seats = cursor.fetchone()[0]
        new_available_seats = available_seats + num_tickets

        update_event_query = "update event set available_seats = ? where event_id = ?"
        cursor.execute(update_event_query, (new_available_seats, event_id))

        # Delete the booking
        delete_query = "delete from booking where booking_id = ?"
        cursor.execute(delete_query, (booking_id,))

        connection.commit()
        connection.close()  # Close the connection after operations
        print(f"Booking {booking_id} canceled and tickets refunded.")

    def get_booking_details(self, booking_id):
        connection = DBConnection.getConnection()  # Open a new connection
        cursor = connection.cursor()
        
        query = "select * from booking where booking_id = ?"
        cursor.execute(query, (booking_id,))
        booking = cursor.fetchone()
        
        connection.close()  # Close the connection after use

        if booking:
            return booking
        else:
            raise InvalidBookingIDException(f"Booking ID '{booking_id}' is invalid.")
