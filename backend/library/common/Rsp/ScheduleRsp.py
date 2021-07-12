class SearchSchedulesRsp():
    def __init__(self, schedules):
        self.schedules = schedules


    def serialzie(self):
        return {"schedules": self.schedules}