class UserData:
    def __init__(self, date, name, category, amount):
        self.date = date
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):
        return(f"<Data: {self.date}, {self.name}, {self.category}, ₹{self.amount:.2f}/-")