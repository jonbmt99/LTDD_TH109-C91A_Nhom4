class CreateCategoryReq(object):
    def __init__(self, req):
        self.category_name = req['category_name'] if 'category_name' in req else None
        self.description = req['description'] if 'description' in req else None
        self.note = req['note'] if 'note' in req else None


class UpdateCategoryReq(object):
    def __init__(self, req):
        self.category_id = req['category_id'] if 'category_id' in req else None
        self.category_name = req['category_name'] if 'category_name' in req else None
        self.description = req['description'] if 'description' in req else None
        self.note = req['note'] if 'note' in req else None


class DeleteCategoryByIdReq():
    def __init__(self, req):
        self.category_id = req['category_id'] if 'category_id' in req else None


class SearchCategoryReq():
    def __init__(self, req):
        self.category_id = req['category_id'] if 'category_id' in req else None
        self.category_name = req['category_name'] if 'category_name' in req else None




