from sqlalchemy import or_

from library import db
from library.common.Req.ScheduleReq import CreateScheduleReq, UpdateScheduleReq, SearchSchedulesReq
from library.DAL import models
from flask import jsonify, json
from library.common.util import ConvertModelListToDictList
from library.common.Req import GetItemsByPageReq
from datetime import datetime


def GetScheduleByPage(req: GetItemsByPageReq):
    schedule_pagination = models.Schedules.query.filter(models.Schedules.delete_at == None).paginate(per_page=req.per_page, page=req.page)
    has_next = schedule_pagination.has_next
    has_prev = schedule_pagination.has_prev
    schedules = ConvertModelListToDictList(schedule_pagination.items)
    return has_next, has_prev, schedules


def CreateSchedule(req: CreateScheduleReq):
    create_schedule = models.Schedules(employee_id=req.employee_id,
                                       date=req.date,
                                       time_from=req.time_from,
                                       time_to=req.time_to,
                                       note=req.note,
                                       actual_hours=req.actual_hours,
                                       expected_hours=req.expected_hours,
                                       salary=req.salary,
                                       delete_at=req.delete_at)
    db.session.add(create_schedule)
    db.session.commit()
    return create_schedule.serialize()


def UpdateSchedule(req: UpdateScheduleReq):
    employee = models.Employees.query.get(req.employee_id)
    update_schedule = models.Schedules.query.get(req.schedule_id)
    update_schedule.employee_id = req.employee_id
    update_schedule.date = req.date
    update_schedule.time_from = req.time_from
    update_schedule.time_to = req.time_to
    update_schedule.note = req.note
    update_schedule.actual_hours = req.actual_hours
    update_schedule.expected_hours = req.expected_hours
    update_schedule.salary = employee.basic_rate * req.actual_hours
    update_schedule.delete_at = req.delete_at
    db.session.commit()
    return update_schedule.serialize()


def SearchSchedules(req: SearchSchedulesReq):
    search_schedules = models.Schedules.query.filter(or_(models.Schedules.schedule_id == req.schedule_id,
                                                         models.Schedules.employee_id == req.employee_id
                                                     )).all()

    schedules = ConvertModelListToDictList(search_schedules)
    return schedules
