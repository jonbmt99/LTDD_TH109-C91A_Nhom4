class CreateOrderDetailReq():
    def __init__(self, req):
        self.order_id = req['order_id'] if 'order_id' in req else None
        self.book_id = req['book_id'] if 'book_id' in req else None
        self.retail_price = req['retail_price'] if 'retail_price' in req else None
        self.quantity = req['quantity'] if 'quantity' in req else None
        self.discount = req['discount'] if 'discount' in req else None
        self.total = req['total'] if 'total' in req else None
        self.note = req['note'] if 'note' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None
