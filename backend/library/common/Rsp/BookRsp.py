class CreateBookRsp():
    def __init__(self, req):
        self.book_id = req.book_id
        self.book_name = req.book_name
        self.supplier_id = req.supplier_id
        self.category_id = req.category_id
        self.author_id = req.author_id
        self.old_amount = req.old_amount
        self.new_amount = req.new_amount
        self.image = req.image
        self.page_number = req.page_number
        self.description = req.description
        self.cost_price = req.cost_price
        self.retail_price = req.retail_price
        self.discount = req.discount
        self.ranking = req.ranking

    def serialize(self):
        return {"book_name": self.book_name, "book_id": self.book_id,
                "supplier_id": self.supplier_id, "category_id": self.category_id, "author_id": self.author_id,
                "old_amount": self.old_amount, "new_amount": self.new_amount, "image": self.image,
                "page_number": self.page_number, "description": self.description, "cost-price": self.cost_price,
                "retail_price": self.retail_price, "discount": self.discount, "ranking": self.ranking}


class DeleteBookByIdRsp():
    def __init__(self, req):
        self.book_id = req.book_id

    def serialize(self):
        return {"book_id": self.book_id}


class UpdateBookRsp():
    def __init__(self, req):
        self.book_id = req.book_id
        self.book_name = req.book_name
        self.supplier_id = req.supplier_id
        self.category_id = req.category_id
        self.author_id = req.author_id
        self.old_amount = req.old_amount
        self.new_amount = req.new_amount
        self.image = req.image
        self.page_number = req.page_number
        self.description = req.description
        self.cost_price = req.cost_price
        self.retail_price = req.retail_price
        self.discount = req.discount
        self.ranking = req.ranking
        self.note = req.note

    def serialize(self):
        return {"book_id": self.book_id, "book_name": self.book_name, "note": self.note,
                "supplier_id": self.supplier_id, "category_id": self.category_id, "author_id": self.author_id,
                "old_amount": self.old_amount, "new_amount": self.new_amount, "image": self.image,
                "page_number": self.page_number, "description": self.description, "cost-price": self.cost_price,
                "retail_price": self.retail_price, "discount": self.discount, "ranking": self.ranking}


class SearchBookByIdRsp():
    def __init__(self, req):
        self.book_name = req.book_name
        self.supplier_id = req.supplier_id
        self.category_id = req.category_id
        self.author_id = req.author_id
        self.old_amount = req.old_amount
        self.new_amount = req.new_amount
        self.image = req.image
        self.page_number = req.page_number
        self.description = req.description
        self.cost_price = req.cost_price
        self.retail_price = req.retail_price
        self.discount = req.discount
        self.ranking = req.ranking

    def serialize(self):
        return {"book_name": self.book_name,
                "supplier_id": self.supplier_id, "category_id": self.category_id, "author_id": self.author_id,
                "old_amount": self.old_amount, "new_amount": self.new_amount, "image": self.image,
                "page_number": self.page_number, "description": self.description, "cost-price": self.cost_price,
                "retail_price": self.retail_price, "discount": self.discount, "ranking": self.ranking}


class SearchBookRsp():
    def __init__(self, books):
        self.books = books

    def serialize(self):
        return {"books": self.books}


