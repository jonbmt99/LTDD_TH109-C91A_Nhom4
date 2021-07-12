class GetMessagesInConversationByFilterReq():
    def __init__(self, req):
        self.page = req['page'] if 'page' in req else 0
        self.per_page = req['per_page'] if 'per_page' in req else 0
        self.conversation_id = req['conversation_id'] if 'conversation_id' in req else 0


class SendMessageReq():
    def __init__(self, req):
        self.conversation_id = req['conversation_id'] if 'conversation_id' in req else None
        self.content = req['content'] if 'content' in req else ''
        self.account_id = req['account_id'] if 'account_id' in req else None

class GetConversationByCustomerAccountIdReq():
    def __init__(self, req):
        self.customer_account_id = req['customer_account_id'] if 'customer_account_id' in req else None

class ReadConversationReq():
    def __init__(self, req):
        self.conversation_id = req['conversation_id'] if 'conversation_id' in req else 0
