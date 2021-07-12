from library.DAL import ScheduleRep, EmployeeRep


def GetScheduleByPage(req):
    has_next, has_prev, schedules = ScheduleRep.GetScheduleByPage(req)
    result = {
        "has_next": has_next,
        "has_prev": has_prev,
        "schedules": schedules
    }
    return result


def CreateSchedule(req):
    create_schedule = ScheduleRep.CreateSchedule(req)
    return create_schedule

def UpdateSchedule(req):
    update_schedule = ScheduleRep.UpdateSchedule(req)
    return update_schedule


def SearchSchedules(req):
    search_schedules = ScheduleRep.SearchSchedules(req)
    return search_schedules
