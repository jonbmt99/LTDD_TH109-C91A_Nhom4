class SearchCategoryRsp():
    def __init__(self, categories):
        self.categories = categories

    def serialize(self):
        return {"categories": self.categories}
