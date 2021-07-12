class CreateEmployeeReq():
    def __init__(self, req):
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.last_name = req['last_name'] if 'last_name' in req else None
        self.first_name = req['first_name'] if 'first_name' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.email = req['email'] if 'email' in req else None
        self.birth_date = req['birth_date'] if 'birth_date' in req else None
        self.hire_date = req['hire_date'] if 'hire_date' in req else None
        self.address = req['address'] if 'address' in req else None
        self.gender = req['gender'] if 'gender' in req else None
        self.image = req['image'] if 'image' in req else None
        self.basic_rate = req['basic_rate'] if 'basic_rate' in req else None
        self.note = req['note'] if 'note' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None


class UpdateEmployeeReq():
    def __init__(self, req):
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.last_name = req['last_name'] if 'last_name' in req else None
        self.first_name = req['first_name'] if 'first_name' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.birth_date = req['birth_date'] if 'birth_date' in req else None
        self.hire_date = req['hire_date'] if 'hire_date' in req else None
        self.address = req['address'] if 'address' in req else None
        self.gender = req['gender'] if 'gender' in req else None
        self.email = req['email'] if 'email' in req else None
        self.image = req['image'] if 'image' in req else None
        self.basic_rate = req['basic_rate'] if 'basic_rate' in req else None
        self.note = req['note'] if 'note' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None


class DeleteEmployeeReq():
    def __init__(self, req):
        self.employee_id = req['employee_id'] if 'employee_id' in req else None


class SearchEmployeesReq():
    def __init__(self, req):
        self.first_name = req['first_name'] if 'first_name' in req else None
        self.last_name = req['last_name'] if 'last_name' in req else None
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
