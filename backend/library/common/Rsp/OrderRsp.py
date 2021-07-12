class SearchOrdersRsp():
    def __init__(self, orders):
        self.orders = orders

    def serialize(self):
        return {"orders": self.orders}

