class CreateSupplierReq():
    def __init__(self, req):
        self.contact_name = req['contact_name'] if 'contact_name' in req else None
        self.address = req['address'] if 'address' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.email = req['email'] if 'email' in req else None
        self.note = req['note'] if 'note' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None


class UpdateSupplierReq():
    def __init__(self, req):
        self.supplier_id = req['supplier_id'] if 'supplier_id' in req else None
        self.contact_name = req['contact_name'] if 'contact_name' in req else None
        self.address = req['address'] if 'address' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.email = req['email'] if 'email' in req else None
        self.note = req['note'] if 'note' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None


class SearchSuppliersReq():
    def __init__(self, req):
        self.supplier_id = req['supplier_id'] if 'supplier_id' in req else None
        self.contact_name = req['contact_name'] if 'contact_name' in req else None

class DeleteSupplierReq():
    def __init__(self, req):
        self.supplier_id = req['supplier_id'] if 'supplier_id' in req else None
