class CreateAuthorReq():
    def __init__(self, req):
        self.author_name = req['author_name'] if 'author_name' in req else None


class DeleteAuthorByIdReq():
    def __init__(self, req):
        self.author_id = req['author_id'] if 'author_id' in req else None


class UpdateAuthorReq():
    def __init__(self, req):
        self.author_id = req['author_id'] if 'author_id' in req else None
        self.author_name = req['author_name'] if 'author_name' in req else None


class SearchAuthorReq:
    def __init__(self, req):
        self.author_id = req['author_id'] if 'author_id' in req else None
        self.author_name = req['author_name'] if 'author_name' in req else None
