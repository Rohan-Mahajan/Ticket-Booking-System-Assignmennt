from entity.venue import Venue
from entity.customer import Customer
from datetime import datetime
from entity.movie import Movie
from entity.concert import Concert
from entity.sports import Sports
from util.db_connection import DBConnection 
from dao.event_service_provider_impl import EventServiceProviderImpl
from dao.booking_system_service_provider_impl import BookingSystemServiceProviderImpl
from exception.event_not_found_exception import EventNotFoundException
from exception.invalid_booking_id_exception import InvalidBookingIDException
from exception.null_pointer_exception import NullPointerException

def main_menu():
    event_service = EventServiceProviderImpl()
    booking_service = BookingSystemServiceProviderImpl()

    while True:
        try:
            print("\n========= Ticket Booking System =========")
            print("1. Create Event")
            print("2. View Event Details")
            print("3. Book Tickets")
            print("4. Cancel Booking")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                create_event(event_service)
            elif choice == "2":
                view_event_details(event_service)
            elif choice == "3":
                book_tickets(booking_service)
            elif choice == "4":
                cancel_booking(booking_service)
            elif choice == "5":
                print("Exiting the system.")
                break
            else:
                print("Invalid choice! Please try again.")

        except NullPointerException as e:
            print(f"Error: {e}")

def create_event(event_service):
    print("\n---- Create Event ----")
    event_name = input("Enter event name: ")
    event_type = input("Enter event type (Movie, Concert, Sports): ").lower()
    event_date = input("Enter event date (YYYY-MM-DD): ")
    event_time = input("Enter event time (HH:MM:SS): ")
    
    # Validate and convert date and time
    try:
        # Check if the input date and time are in the correct format
        event_date = datetime.strptime(event_date, '%Y-%m-%d').date()  # Convert to date
        event_time = datetime.strptime(event_time, '%H:%M:%S').time()  # Convert to time
    except ValueError as ve:
        print(f"Invalid date or time format: {ve}")
        return

    venue_name = input("Enter venue name: ")
    venue_address = input("Enter venue address: ")
    total_seats = int(input("Enter total seats: "))
    available_seats = total_seats
    ticket_price = float(input("Enter ticket price: "))

    # Connect to the database
    connection = DBConnection.getConnection()
    cursor = connection.cursor()

    # Check if the venue already exists
    cursor.execute("select venue_id from venue where venue_name = ?", (venue_name,))
    venue_data = cursor.fetchone()

    if venue_data:
        venue_id = venue_data[0]  # Use existing venue_id
        print(f"Using existing venue: {venue_name} (ID: {venue_id})")
    else:
        # Insert the new venue into the venue table
        insert_venue_query = """
        insert into venue (venue_name, address) 
        values (?, ?);
        """
        cursor.execute(insert_venue_query, (venue_name, venue_address))
        connection.commit()  # Commit the new venue insertion

        # Retrieve the last inserted venue_id
        cursor.execute("select scope_identity();")
        venue_id = cursor.fetchone()[0]  # Get the venue_id of the newly added venue
        print(f"New venue '{venue_name}' added with ID: {venue_id}")

    # Create the event based on its type
    if event_type == "movie":
        genre = input("Enter genre: ")
        actor = input("Enter lead actor: ")
        actress = input("Enter lead actress: ")
        print(f"Creating Movie Event with venue_id: {venue_id}")  # Debugging statement
        event = Movie(event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, genre, actor, actress)

    elif event_type == "concert":
        artist = input("Enter artist name: ")
        concert_type = input("Enter concert type: ")
        print(f"Creating Concert Event with venue_id: {venue_id}")  # Debugging statement
        event = Concert(event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, artist, concert_type)

    elif event_type == "sports":
        sport_name = input("Enter sport name: ")
        teams_name = input("Enter teams (e.g., 'Team A vs Team B'): ")
        print(f"Creating Sports Event with venue_id: {venue_id}")  # Debugging statement
        event = Sports(event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, sport_name, teams_name)

    else:
        print("Invalid event type! Event creation failed.")
        return

    # Now use the event_service to create the event
    event_service.create_event(event)

    # Close the database connection
    connection.close()

def view_event_details(event_service):
    print("\n---- View Event Details ----")
    events = event_service.get_event_details()
    if events:
        for event in events:
            print(event)
    else:
        print("No events found.")

def book_tickets(booking_service):
    try:
        print("\n---- Book Tickets ----")
        event_name = input("Enter event name to book tickets for: ")
        
        # Gather customer details
        customer_name = input("Enter your name: ")
        email = input("Enter your email: ")
        phone = input("Enter your phone number: ")
        num_tickets = int(input("Enter number of tickets to book: "))

        # Create a dictionary to hold customer details
        customer_details = {
            'name': customer_name,
            'email': email,
            'phone': phone
        }

        # Call the booking service to book tickets for the event
        booking_service.book_tickets(event_name, customer_details, num_tickets)
    
    except EventNotFoundException as e:
        print(e)

    except ValueError as ve:
        print(f"Invalid input: {ve}")

def cancel_booking(booking_service):
    try:
        print("\n---- Cancel Booking ----")
        booking_id = int(input("Enter booking ID to cancel: "))
        booking_service.cancel_booking(booking_id)
    
    except InvalidBookingIDException as e:
        print(e)
    
    except ValueError as ve:
        print(f"Invalid input: {ve}")

if __name__ == "__main__":
    main_menu()
