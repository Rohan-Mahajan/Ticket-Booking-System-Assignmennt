class NullPointerException(Exception):
    def __init__(self, message="Null pointer encountered"):
        self.message = message
        super().__init__(self.message)
