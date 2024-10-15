class PropertyUtil:
    
    @staticmethod
    def getConnectionString():
        return (
            'Driver={SQL Server};'
            'Server=MYIDEAPAD\\SQLEXPRESS;'  # Adjust to your server details
            'Database=ticketbookingsystem;'  # Adjust to your database name
            'Trusted_Connection=yes;'  # This uses Windows Authentication
        )
