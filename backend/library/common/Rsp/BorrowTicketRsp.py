class SearchBorrowTicketRsp():
    def __init__(self, borrow_tickets):
        self.borrow_tickets = borrow_tickets

    def serialize(self):
        return {"borrow_tickets": self.borrow_tickets}
