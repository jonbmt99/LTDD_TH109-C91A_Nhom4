class ErrorRsp(Exception):
    def __init__(self, code, message, msg):
        self.code = code
        self.message = message
        self.msg = msg
        super().__init__(self.message)
