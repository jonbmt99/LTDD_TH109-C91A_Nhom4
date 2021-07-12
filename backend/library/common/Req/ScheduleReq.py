class CreateScheduleReq():
    def __init__(self, req):
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
        self.date = req['date'] if 'date' in req else None
        self.time_from = req['time_from'] if 'time_from' in req else None
        self.time_to = req['time_to'] if 'time_to' in req else None
        self.note = req['note'] if 'note' in req else None
        self.actual_hours = req['actual_hours'] if 'actual_hours' in req else None
        self.expected_hours = req['expected_hours'] if 'expected_hours' in req else None
        self.salary = req['salary'] if 'salary' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None


class UpdateScheduleReq():
    def __init__(self, req):
        self.schedule_id = req['schedule_id'] if 'schedule_id' in req else None
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
        self.date = req['date'] if 'date' in req else None
        self.time_from = req['time_from'] if 'time_from' in req else None
        self.time_to = req['time_to'] if 'time_to' in req else None
        self.note = req['note'] if 'note' in req else None
        self.actual_hours = req['actual_hours'] if 'actual_hours' in req else None
        self.expected_hours = req['expected_hours'] if 'expected_hours' in req else None
        self.salary = req['salary'] if 'salary' in req else None
        self.delete_at = req['delete_at'] if 'delete_at' in req else None


class SearchSchedulesReq():
    def __init__(self, req):
        self.schedule_id = req['schedule_id'] if 'schedule_id' in req else None
        self.employee_id = req['employee_id'] if 'employee_id' in req else None
