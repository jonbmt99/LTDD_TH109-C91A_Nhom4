class GetItemsByPageRsp():
    def __init__(self, has_next=False, has_prev=False, items=[], currentPage=None):
        self.has_next = has_next
        self.has_prev = has_prev
        self.items = items
        self.current_page = currentPage if currentPage else None

    def serialize(self):
        return {
            "has_next": self.has_next,
            "has_prev": self.has_prev,
            "items": self.items,
            "current_page": self.current_page,
        }
