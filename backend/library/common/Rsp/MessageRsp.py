class SendMessageRsp():
    def __init__(self, req):
        self.message_id = req['message_id'] if req['message_id'] else None
        self.conversation_id = req['conversation_id'] if req['conversation_id'] else None
        self.content = req['content'] if req['content'] else None
        self.account_id = req['account_id'] if req['account_id'] else None
        self.created_at = req['created_at'] if req['created_at'] else None
        self.is_read = req['is_read'] == True if True else False

    def serialize(self):
        return {"conversation_id": self.conversation_id,
                "content": self.content,
                "account_id": self.account_id,
                "message_id": self.message_id,
                "is_read": self.is_read,
                "created_at": str(self.created_at)
                }
