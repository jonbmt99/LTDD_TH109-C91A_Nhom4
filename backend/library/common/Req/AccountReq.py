class CreateAccountReq():
    def __init__(self, req):
        self.role_id = req['role_id'] if 'role_id' in req else None
        self.account_name = req['account_name'] if 'account_name' in req else None
        self.account_password = req['account_password'] if 'account_password' in req else None
        self.confirm_account_password = req['confirm_account_password'] if 'confirm_account_password' in req else None
        self.deleted_at = req['deleted_at'] if 'deleted_at' in req else None
        self.note = req['note'] if 'note' in req else None


class DeleteAccountReq():
    def __init__(self, req):
        self.account_id = req['account_id'] if 'account_id' in req else ''
        self.account_name = req['account_name'] if 'account_name' in req else ''

    def serialize(self):
        return {
            "account_name": self.account_name,
            "account_id": self.account_id
        }


class LoginReq():
    def __init__(self, req):
        self.user_name = req['user_name']
        self.password = req['password']


class LoginRsp():
    def __init__(self, req):
        self.access_token = req['access_token'] if 'access_token' in req else None
        self.user_info = req['user_info'] if 'user_info' in req else None
        self.account = req['account'] if 'account' in req else None

    def serialize(self):
        return {
            "access_token": self.access_token.decode('utf-8'),
            "user_info": self.user_info,
            "account": self.account
        }


class SearchAccountsReq():
    def __init__(self, req):
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.account_name = req['account_name'] if 'account_name' in req else None


class SendResetPasswordEmailReq():
    def __init__(self, req):
        self.email = req['email'] if 'email' in req else None


class ResetPasswordReq():
    def __init__(self, req):
        self.token = req['token'] if 'token' in req else None
        self.password = req['password'] if 'password' in req else None


class ChangePasswordReq():
    def __init__(self, req):
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.current_password = req['current_password'] if 'current_password' in req else None
        self.new_password = req['new_password'] if 'new_password' in req else None


class CreateCustomerAccountReq():
    def __init__(self, req):
        # account
        self.account_name = req['account_name'] if 'account_name' in req else None
        self.role_id = req['role_id'] if 'role_id' in req else None
        self.account_password = req['account_password'] if 'account_password' in req else None
        # customer
        self.account_id = req['account_id'] if 'account_id' in req else None
        self.last_name = req['last_name'] if 'last_name' in req else None
        self.first_name = req['first_name'] if 'first_name' in req else None
        self.email = req['email'] if 'email' in req else None
        self.phone = req['phone'] if 'phone' in req else None
        self.birth_date = req['birth_date'] if 'birth_date' in req else None
        self.address = req['address'] if 'address' in req else None
        self.gender = req['gender'] if 'gender' in req else None
        self.province_id = req['province_id'] if 'province_id' in req else None
        self.district_id = req['district_id'] if 'district_id' in req else None
        self.ward_id = req['ward_id'] if 'ward_id' in req else None
        self.image = req['image'] if 'image' in req else None


class CreateEmployeeAccountReq():
    def __init__(self, req):
        # account
        self.account_name = req['account_name'] if 'account_name' in req else None
        self.role_id = req['role_id'] if 'role_id' in req else None
        self.account_password = req['account_password'] if 'account_password' in req else None
        # Employee
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
        self.province_id = req['province_id'] if 'province_id' in req else None
        self.district_id = req['district_id'] if 'district_id' in req else None
        self.ward_id = req['ward_id'] if 'ward_id' in req else None
