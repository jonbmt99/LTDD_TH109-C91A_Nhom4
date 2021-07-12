class CreateCustomerReq():
    def __init__(self, req):
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.last_name = req['last_name'] if 'last_name' in req else None
        self.first_name = req['first_name'] if 'first_name' in req else None
        self.email = req['email'] if 'email' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.birth_date = req['birth_date'] if 'birth_date' in req else None
        self.address = req['address'] if 'address' in req else None
        self.gender = req['gender'] if 'gender' in req else None
        self.note = req['note'] if 'note' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None
        self.image = req['image'] if 'image' in req else None
        self.province_id = req['province_id'] if 'province_id' in req else None
        self.district_id = req['district_id'] if 'district_id' in req else None
        self.ward_id = req['ward_id'] if 'ward_id' in req else None

class UpdateCustomerReq():
    def __init__(self, req):
        self.customer_id = req['customer_id'] if 'customer_id' in req else None
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.last_name = req['last_name'] if 'last_name' in req else None
        self.first_name = req['first_name'] if 'first_name' in req else None
        self.email = req['email'] if 'email' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.birth_date = req['birth_date'] if 'birth_date' in req else None
        self.image = req['image'] if 'image' in req else None
        self.address = req['address'] if 'address' in req else None
        self.gender = req['gender'] if 'gender' in req else None
        self.note = req['note'] if 'note' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None

        self.province_id = req['province_id'] if 'province_id' in req else None
        self.district_id = req['district_id'] if 'district_id' in req else None
        self.ward_id = req['ward_id'] if 'ward_id' in req else None

class DeleteCustomerReq():
    def __init__(self, req):
        self.customer_id = req['customer_id'] if 'customer_id' in req else None


class SearchCustomersReq():
    def __init__(self, req):
        self.customer_id = req['customer_id'] if 'customer_id' in req else None
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.phone = req['phone'] if 'phone' in req else None
