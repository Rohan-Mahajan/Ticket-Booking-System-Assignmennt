from util.db_connection import DBConnection  # Updated import to use the new DBConnection class

class EventServiceProviderImpl:

    def create_event(self, event):
        connection = DBConnection.getConnection()  # Using DBConnection to get the connection
        cursor = connection.cursor()
    
        # Prepare the SQL query
        query = """
        insert into event (event_name, event_date, event_time, venue_id, total_seats, available_seats, ticket_price, event_type) 
        values (?, ?, ?, ?, ?, ?, ?, ?)
        """
        
        # Ensure event_date is a string in 'YYYY-MM-DD' format and event_time is a string in 'HH:MM:SS' format
        cursor.execute(query, (
            event.event_name,
            event.event_date.isoformat(),  # Ensure this is in the correct format
            event.event_time.strftime('%H:%M:%S'),  # Ensure this is in the correct format
            event.venue_id,
            event.total_seats,
            event.available_seats,
            event.ticket_price,
            event.event_type
        ))
    
        connection.commit()
        connection.close()
        print(f"Event '{event.event_name}' created successfully.")
    
    
    def get_event_details(self):
        connection = DBConnection.getConnection()  # Using DBConnection to get the connection
        cursor = connection.cursor()
        
        query = "select * from event"
        cursor.execute(query)
        events = cursor.fetchall()
        
        connection.close()
        return events
    
    def get_available_tickets(self, event_name):
        connection = DBConnection.getConnection()  # Using DBConnection to get the connection
        cursor = connection.cursor()
        
        query = "select available_seats from event where event_name = ?"
        cursor.execute(query, (event_name,))
        result = cursor.fetchone()
        
        connection.close()
        if result:
            return result[0]
        else:
            return None
