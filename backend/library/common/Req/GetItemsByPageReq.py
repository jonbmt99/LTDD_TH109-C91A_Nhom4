class GetItemsByPageReq():
    def __init__(self, req):
        self.page = req['page']
        self.per_page = req['per_page']


class SearchItemsReq():
    def __init__(self, req):
        self.order_id = req['order_id'] if 'order_id' in req else None
        self.contact_name = req['contact_name'] if 'contact_name' in req else None
        self.customer_phone = req['customer_phone'] if 'customer_phone' in req else None
        self.type = req['type'] if 'type' in req else None
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.customer_id = req['customer_id'] if 'customer_id' in req else None
        self.customer_name = req['customer_name'] if 'customer_name' in req else None
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
        self.email = req['email'] if 'email' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.account_name = req['account_name'] if 'account_name' in req else None
        self.role_id = req['role_id'] if 'role_id' in req else None
        self.book_id = req['book_id'] if 'book_id' in req else None
        self.id = req['id'] if 'id' in req else None
        self.book_name = req['book_name'] if 'book_name' in req else None
        self.author_id = req['author_id'] if 'author_id' in req else 0
        self.category_id = req['category_id'] if 'category_id' in req else 0
        self.supplier_id = req['supplier_id'] if 'supplier_id' in req else 0
        self.borrow_ticket_id = req['borrow_ticket_id'] if 'borrow_ticket_id' in req else 0
        self.borrow_ticket_status = req['borrow_ticket_status'] if 'borrow_ticket_status' in req else None