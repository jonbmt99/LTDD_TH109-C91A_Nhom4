class CreateBookReq(object):
    def __init__(self, req):
        self.book_name = req['book_name'] if 'book_name' in req else None
        self.supplier_id = req['supplier_id'] if 'supplier_id' in req else None
        self.category_id = req['category_id'] if 'category_id' in req else None
        self.author_id = req['author_id'] if 'author_id' in req else None
        self.old_amount = req['old_amount'] if 'old_amount' in req else None
        self.new_amount = req['new_amount'] if 'new_amount' in req else None
        self.image = req['image'] if 'image' in req else None
        self.page_number = req['page_number'] if 'page_number' in req else None
        self.description = req['description'] if 'description' in req else None
        self.cost_price = req['cost_price'] if 'cost_price' in req else None
        self.retail_price = req['retail_price'] if 'retail_price' in req else None
        self.discount = req['discount'] if 'discount' in req else 0
        self.ranking = req['ranking'] if 'ranking' in req else None


class DeleteBookByIdReq():
    def __init__(self, req):
        self.book_id = req['book_id'] if 'book_id' in req else None


class UpdateBookReq():
    def __init__(self, req):
        self.book_id = req['book_id'] if 'book_id' in req else None
        self.book_name = req['book_name'] if 'book_name' in req else None
        self.supplier_id = req['supplier_id'] if 'supplier_id' in req else 0
        self.category_id = req['category_id'] if 'category_id' in req else 0
        self.author_id = req['author_id'] if 'author_id' in req else 0
        self.old_amount = req['old_amount'] if 'old_amount' in req else None
        self.new_amount = req['new_amount'] if 'new_amount' in req else None
        self.image = req['image'] if 'image' in req else None
        self.page_number = req['page_number'] if 'page_number' in req else None
        self.description = req['description'] if 'description' in req else None
        self.cost_price = req['cost_price'] if 'cost_price' in req else None
        self.retail_price = req['retail_price'] if 'retail_price' in req else None
        self.discount = req['discount'] if 'discount' in req else None
        self.ranking = req['ranking'] if 'ranking' in req else None
        self.note = req['note'] if 'note' in req else None


class SearchBookReq:
    def __init__(self, req):
        self.book_id = req['book_id'] if 'book_id' in req else None
        self.retail_price = req['retail_price'] if 'retail_price' in req else None
        self.from_price = req['from_price'] if 'from_price' in req else None
        self.to_price = req['to_price'] if 'to_price' in req else None
        self.id = req['id'] if 'id' in req else None
        self.book_name = req['book_name'] if 'book_name' in req else None
        self.author_id = req['author_id'] if 'author_id' in req else None
        self.category_id = req['category_id'] if 'category_id' in req else None
        self.supplier_id = req['supplier_id'] if 'supplier_id' in req else None
