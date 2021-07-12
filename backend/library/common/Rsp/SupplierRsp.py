class SearchSuppliersRsp():
    def __init__(self, suppliers):
        self.suppliers = suppliers

    def serialize(self):
        return {"suppliers": self.suppliers}
