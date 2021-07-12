from library import app
from library.BLL import EmployeeSvc
from library.DAL import models
from library.common.Req.EmployeeReq import CreateEmployeeReq, UpdateEmployeeReq, DeleteEmployeeReq, SearchEmployeesReq
from library.common.Req.GetItemsByPageReq import GetItemsByPageReq, SearchItemsReq
from library.common.Rsp.EmployeeRsp import SearchEmployeeRsp
from library.common.Rsp.GetImtesByPageRsp import GetItemsByPageRsp
from flask import jsonify, request, make_response
import json

from library.common.Rsp.SingleRsp import ErrorRsp
from library.common.util import ConvertModelListToDictList


@app.route('/admin/employee-management/get-employees', methods=['POST', 'GET'])
def GetEmployees():
    req = GetItemsByPageReq(request.json)
    result = EmployeeSvc.GetEmployeesByPage(req)
    res = GetItemsByPageRsp(has_next=result['has_next'], has_prev=result['has_prev'],
                            items=result['employees']).serialize()
    return jsonify(res)


@app.route('/admin/employee-management/create-employee', methods=['POST'])
def CreateEmployee():
    req = CreateEmployeeReq(request.json)
    result = EmployeeSvc.CreateEmployee(req)
    return jsonify(result)


@app.route('/admin/employee-management/update-employee', methods=['POST'])
def UpdateEmployee():
    req = UpdateEmployeeReq(request.json)
    result = EmployeeSvc.UpdateEmployee(req)
    return jsonify(result)


@app.route('/admin/employee-management/delete-employee', methods=['POST'])
def DeleteEmployee():
    req = DeleteEmployeeReq(request.json)
    result = EmployeeSvc.DeleteEmployee(req)
    return jsonify(result)


@app.route('/admin/employee-management/search-employees', methods=['POST', 'GET'])
def SearchEmployees():
    req = SearchItemsReq(request.json)
    if (req.employee_id):
        employees = models.Employees.query.filter(models.Employees.employee_id == req.employee_id, models.Employees.delete_at == None)
        return jsonify(ConvertModelListToDictList(employees.all()))

    employees = models.Employees.query
    if req.phone != None:
        employees = employees.filter(models.Employees.phone.contains(req.phone))

    employees = employees.filter(models.Employees.delete_at == None)
    employees = ConvertModelListToDictList(employees.all())
    return jsonify(employees)

