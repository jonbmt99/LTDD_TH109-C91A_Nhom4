class SearchEmployeeRsp():
    def __init__(self, employees):
        self.employees = employees

    def serialize(self):
        return {"employees": self.employees}

