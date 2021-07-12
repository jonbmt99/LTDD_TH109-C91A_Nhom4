class CreateAccountRsp():
    def __init__(self, req):
        self.account_name = req.account_name
        self.role_id = req.role_id

    def serialize(self):
        return {
            "account_name": self.account_name,
            "role_id": self.role_id,
        }

class SearchAccountsRsp():
    def __init__(self, accounts):
        self.accounts = accounts
    def serialize(self):
        return {
            "accounts": self.accounts,
        }
