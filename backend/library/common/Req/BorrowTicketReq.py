class CreateBorrowTicketReq():
    def __init__(self, req):
        self.customer_id = req['customer_id'] if 'customer_id' in req else None
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
        self.borrow_book_ids = req['borrow_book_ids'] if 'borrow_book_ids' in req else None
        self.note = req['note'] if 'note' in req else None


class UpdateBorrowTicketReq():
    def __init__(self, req):
        self.borrow_ticket_id = req['borrow_ticket_id'] if 'borrow_ticket_id' in req else None
        self.customer_id = req['customer_id'] if 'customer_id' in req else None
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
        self.quantity = req['quantity'] if 'quantity' in req else None
        self.borrow_date = req['borrow_date'] if 'borrow_date' in req else None
        self.appointment_date = req['appointment_date'] if 'appointment_date' in req else None
        self.return_date = req['return_date'] if 'return_date' in req else None
        self.status = req['status'] if 'status' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None
        self.note = req['note'] if 'note' in req else None


class FinishBorrowTicketReq():
    def __init__(self, req):
        self.borrow_ticket_id = req['borrow_ticket_id'] if 'borrow_ticket_id' in req else None



class DeleteBorrowTicketReq():
    def __init__(self, req):
        self.borrow_ticket_id = req['borrow_ticket_id'] if 'borrow_ticket_id' in req else None

class SendEmailForLateBorrowTicketReq():
    def __init__(self, req):
        self.message = req['message'] if 'message' in req else None
        self.customer_email = req['customer_email'] if 'customer_email' in req else None

class SearchBorrowTicketReq():
    def __init__(self, req):
        self.borrow_ticket_id = req['borrow_ticket_id'] if 'borrow_ticket_id' in req else None
        self.customer_id = req['customer_id'] if 'customer_id' in req else None
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
        self.borrow_date = req['borrow_date'] if 'borrow_date' in req else None
        self.return_date = req['return_date'] if 'return_date' in req else None
        self.status = req['status'] if 'status' in req else None
