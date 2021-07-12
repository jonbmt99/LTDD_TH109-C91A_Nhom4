from datetime import datetime
from time import gmtime, strftime

from sqlalchemy import or_

from library import db
from library.common.Req import GetItemsByPageReq
from library.common.Req.EmployeeReq import CreateEmployeeReq, UpdateEmployeeReq, DeleteEmployeeReq, SearchEmployeesReq
from library.common.Rsp.EmployeeRsp import SearchEmployeeRsp
from library.common.util import ConvertModelListToDictList
from library.DAL import models
from flask import jsonify, json
from datetime import datetime


def GetEmployeesbyPage(req: GetItemsByPageReq):
    employees_pagination = models.Employees.query.filter(models.Employees.delete_at == None).paginate(per_page=req.per_page, page=req.page)
    has_next = employees_pagination.has_next
    has_prev = employees_pagination.has_prev
    employees = ConvertModelListToDictList(employees_pagination.items)
    return has_next, has_prev, employees


def CreateEmployee(req: CreateEmployeeReq):
    create_employee = models.Employees(
                                       account_id=req.account_id,
                                       last_name=req.last_name,
                                       first_name=req.first_name,
                                       phone=req.phone,
                                       email=req.email,
                                       birth_date=req.birth_date,
                                       hire_date=req.hire_date,
                                       address=req.address,
                                       gender=req.gender,
                                       image=req.image,
                                       basic_rate=req.basic_rate,
                                       note=req.note,
                                       delete_at=req.delete_at)
    db.session.add(create_employee)
    db.session.commit()
    return create_employee.serialize()


def UpdateEmployee(req: UpdateEmployeeReq):
    update_employee = models.Employees.query.get(req.employee_id)
    update_employee.account_id = req.account_id if req.account_id is not None else update_employee.account_id
    update_employee.last_name = req.last_name if req.last_name is not None else update_employee.last_name
    update_employee.first_name = req.first_name if req.first_name is not None else update_employee.first_name
    update_employee.email = req.email if req.email is not None else update_employee.email
    update_employee.phone = req.phone if req.phone is not None else update_employee.phone
    update_employee.birth_date = req.birth_date if req.birth_date is not None else update_employee.birth_date
    update_employee.hire_date = req.hire_date if req.hire_date is not None else update_employee.hire_date
    update_employee.address = req.address if req.address is not None else update_employee.address
    update_employee.gender = req.gender if req.gender is not None else update_employee.gender
    update_employee.image = req.image if req.image is not None else update_employee.image
    update_employee.basic_rate = req.basic_rate if req.basic_rate is not None else update_employee.basic_rate
    update_employee.note = req.note if req.note is not None else update_employee.note
    update_employee.delete_at = req.delete_at if req.delete_at is not None else update_employee.delete_at
    db.session.commit()
    return update_employee.serialize()


def DeleteEmployee(req: DeleteEmployeeReq):
    delete_employee = models.Employees.query.get(req.employee_id)
    delete_employee.delete_at = datetime.now()
    db.session.add(delete_employee)
    db.session.commit()

    return delete_employee.serialize()


def SearchEmployees(req: SearchEmployeesReq):
    search_employee = models.Employees.query.filter(or_(models.Employees.first_name == req.first_name,
                                                        models.Employees.last_name == req.last_name,
                                                        models.Employees.account_id == req.account_id,
                                                        models.Employees.phone == req.phone,
                                                        models.Employees.employee_id == req.employee_id)).all()
    employees = ConvertModelListToDictList(search_employee)
    return employees


